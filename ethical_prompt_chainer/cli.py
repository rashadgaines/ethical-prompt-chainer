import click
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
load_dotenv()
from .chainer import EthicalPromptChainer
from .config import get_settings
from .logging import setup_logging
import csv

@click.group()
def cli():
    """Ethical Prompt Chainer CLI."""
    pass

@cli.command()
@click.argument('dilemma')
@click.option('--model', default=None, help='Model name to use')
@click.option('--device', default=None, help='Device to run the model on')
@click.option('--output', type=click.Path(), help='Output file path')
@click.option('--log-file', type=click.Path(), help='Log file path')
def analyze(dilemma: str, model: Optional[str], device: Optional[str], output: Optional[str], log_file: Optional[str]):
    """Analyze an ethical dilemma."""
    # Set up logging
    logger = setup_logging(log_file=log_file)
    logger.info(f"Analyzing dilemma: {dilemma}")
    
    # Get settings
    settings = get_settings()
    if model:
        settings.model.model_name = model
    if device:
        settings.model.device = device
    
    try:
        # Initialize chainer
        chainer = EthicalPromptChainer(
            model_name=settings.model.model_name,
            device=settings.model.device
        )
        
        # Perform analysis
        analysis = chainer.analyze_dilemma(dilemma)
        formatted = chainer.format_analysis(analysis)
        
        # Output results
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(formatted)
            logger.info(f"Results written to {output}")
        else:
            click.echo(formatted)
            
    except Exception as e:
        logger.error(f"Error analyzing dilemma: {str(e)}")
        raise click.ClickException(str(e))

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--models', help='Comma-separated list of models to use (e.g., "gpt-4,grok-3")')
@click.option('--device', default=None, help='Device to run the model on')
@click.option('--output-dir', type=click.Path(), help='Output directory')
@click.option('--log-file', type=click.Path(), help='Log file path')
@click.option('--format', type=click.Choice(['txt', 'csv']), default='txt', help='Output format (txt or csv)')
def batch(input_file: str, models: Optional[str], device: Optional[str], output_dir: Optional[str], log_file: Optional[str], format: str):
    """Analyze multiple dilemmas from a file using multiple models."""
    # Set up logging
    logger = setup_logging(log_file=log_file)
    
    # Read dilemmas
    dilemmas = Path(input_file).read_text().splitlines()
    logger.info(f"Processing {len(dilemmas)} dilemmas from {input_file}")
    
    # Parse models
    model_list = [m.strip() for m in models.split(',')] if models else ["gpt-4", "grok-3"]
    logger.info(f"Using models: {', '.join(model_list)}")
    
    try:
        # Process each model
        for model_name in model_list:
            # Get settings
            settings = get_settings()
            settings.model.model_name = model_name
            if device:
                settings.model.device = device
            
            # Initialize chainer for this model
            chainer = EthicalPromptChainer(
                model_name=settings.model.model_name,
                device=settings.model.device
            )
            
            logger.info(f"Processing dilemmas with model: {model_name}")
            
            # Process each dilemma
            for i, dilemma in enumerate(dilemmas, 1):
                if not dilemma.strip():
                    continue
                    
                logger.info(f"Processing dilemma {i}/{len(dilemmas)} with {model_name}: {dilemma}")
                
                # Perform analysis
                analysis = chainer.analyze_dilemma(dilemma)
                
                # Output results
                if output_dir:
                    if format == 'txt':
                        output_path = Path(output_dir) / f"{model_name}_dilemma_{i}.txt"
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        output_path.write_text(chainer.format_analysis(analysis))
                        logger.info(f"Results written to {output_path}")
                    elif format == 'csv':
                        output_path = Path(output_dir) / "dilemmas.csv"
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # Write header only if file doesn't exist
                        if not output_path.exists():
                            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                writer.writerow(['Model', 'Dilemma', 'Framing', 'Stakeholders', 'Consequences', 'Principles', 'Solution'])
                        
                        # Always append to CSV
                        with open(output_path, 'a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            writer.writerow([
                                model_name,
                                analysis.dilemma,
                                analysis.framing,
                                analysis.stakeholders,
                                analysis.consequences,
                                analysis.principles,
                                analysis.solution
                            ])
                        logger.info(f"Results appended to {output_path}")
                else:
                    click.echo(f"\n{'='*80}\n")
                    click.echo(f"Model: {model_name}")
                    click.echo(chainer.format_analysis(analysis))
                    
    except Exception as e:
        logger.error(f"Error processing dilemmas: {str(e)}")
        raise click.ClickException(str(e))

if __name__ == '__main__':
    cli() 