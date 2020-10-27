# angdist

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4104053.svg)](https://doi.org/10.5281/zenodo.4104053)

Plot the 2D histogram of Euler angles covered by a set of cryo-EM particles.

A single-particle cryo-EM reconstruction comes from a set of particle images
corresponding to projections of identical particles in different orientations.
Knowing how many particles contributed to any given projection orientation is
important to assess the quality of a dataset. This command-line tool generates a
2D histogram of particle orientations from a `run_*_data.star` file from a
RELION Class3D or Refine3D job.

This tool was tested with star files produced by RELION-3.1.0. Earlier versions
of RELION are not supported.

## FAQ

**Q:** Doesn't RELION already do this?

**A:** RELION-3.1 produces a histogram of Euler angles, but in 3D
(`*_angdist.bild` files). This is very convenient to visually relate specific
Euler angles to the corresponding orientation of the 3D reconstruction of the
particle. This tool is complementary to RELION in that it produces a 2D
histogram. A 2D histogram is easier to look at globally, making it easy to
rapidly spot problems (missing orientations, strongly preferred orientations,
etc.). This tool doesn't require an installation of RELION, allowing one to
inspect files quickly from a different computer. This tool also lets you adjust
the number of bins in the histogram, and save the histogram as an SVG file
(which is useful for adjusting styling to make a pretty figure).

**Q:** Doesn't cryoSPARC already do this?

**A:** Yes, cryoSPARC already prints out this exact same histogram. This tool,
however, doesn't require an installation of cryoSPARC, allowing one to inspect
files quickly from a different computer. This tool also lets you adjust the
number of bins in the histogram, and save the histogram as an SVG file (which is
useful for adjusting styling to make a pretty figure). Finally, this tool uses a
default color scale that is much more readable to color blind people than the
one used by cryoSPARC.

## Acknowledgments

I would not have been able to put this tool together without the
[`starfile`](https://github.com/alisterburt/starfile) library.

## Installation

```
$ pip install angdist
```

## Usage

```
$ angdist --help
Usage: angdist [OPTIONS] <run_data.star>

  Plot a 2D histogram of Euler angles distribution from a run_data.star
  file produced by RELION.

Options:
  -t, --title TEXT        Title of the histogram (default: no title).
  -c, --colormap TEXT     A color map supported by matplotlib (default:
                          "viridis").

  -g, --gridsize INTEGER  Number of hexagonal bins along the x axis (default:
                          50).

  -o, --output TEXT       File name to save the histogram (optional: with no
                          file name, simply display the histogram on screen
                          without saving it; recommended file formats: .png,
                          .pdf, .svg or any format supported by matplotlib).

  -h, --help              Show this message and exit.
```
