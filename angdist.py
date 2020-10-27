import starfile as star
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import click

# Building blocks

def load_angles(starfile):
    """Load rlnAngleRot and rlnAngleTilt from a run_data.star file."""
    star_data = star.open(starfile)
    angles = star_data[1][['rlnAngleRot', 'rlnAngleTilt']]
    return angles

def build_histogram(angles, title, colormap, gridsize):
    """Builds a 2D histogram of number of particles per Euler angle pair."""
    fig, ax = plt.subplots()
    hb = ax.hexbin(angles.rlnAngleRot, angles.rlnAngleTilt, bins='log', cmap=colormap, gridsize=gridsize)
    ax.set(xlim=(-180, 180), ylim=(0, 180))
    ax.set_xlabel('$\phi$ (rlnAngleRot, deg)')
    ax.set_xticks(range(-180, 181, 45))
    ax.set_ylabel('$\\theta$ (rlnAngleTilt, deg)')
    ax.set_yticks(range(0, 181, 45))
    ax.set_title(title)
    fig.gca().set_aspect('equal', adjustable='box')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.1)
    cb = fig.colorbar(hb, ax=ax, cax=cax)
    cb.set_label('Number of particles')
    fig.tight_layout()
    return fig

# Command-line tool made from the buidling blocks

@click.command(context_settings = dict(help_option_names=['-h', '--help']))
@click.argument('starfile', metavar='<run_data.star>')
@click.option('-t', '--title', 'title', default='', type=str, help='Title of the histogram (default: no title).')
@click.option('-c', '--colormap', 'colormap', default='viridis', type=str, help='A color map supported by matplotlib (default: "viridis").')
@click.option('-g', '--gridsize', 'gridsize', default=50, type=int, help='Number of hexagonal bins along the x axis (default: 50).')
@click.option('-o', '--output', 'output_file', default='', type=str, help='File name to save the histogram (optional: with no file name, simply display the histogram on screen without saving it; recommended file formats: .png, .pdf, .svg or any format supported by matplotlib).')
def cli(starfile, title, colormap, gridsize, output_file):
    """Plot a 2D histogram of Euler angles distribution from a run_data.star file produced by RELION."""
    angles = load_angles(starfile)
    histogram = build_histogram(angles, title, colormap, gridsize)
    if output_file:
        histogram.figsize = (11.80, 8.85)
        histogram.dpi = 300
        plt.savefig(output_file)
    else:
        plt.show()
