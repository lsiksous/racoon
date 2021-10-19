import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.font_manager
from cycler import cycler

def ft_style():
    #Fonts
    [f.name for f in matplotlib.font_manager.fontManager.ttflist]
    plt.rcParams['font.family'] = 'Fira Mono'

    #Financier Style
    ft_background = "#FFF1E5"
    ft_democratblue = "#0F56B5"
    ft_republicanred = "#EF4647"
    ft_pink = "#E95D8C"
    ft_darkred = "#7D062E"
    ft_darkblue = "#065296"
    ft_blue = "#2591CE"
    ft_lightblue = "#72D9E7"
    ft_greenish = "#A2BC5D"
    ft_maybegrey = "#716962"
    ft_golden = "#B89E17"

    tinyfont = 14
    smallfont = 20
    largefont = 28
    linewidth = 5

    plt.rcParams['figure.facecolor'] = ft_background
    plt.rcParams['axes.facecolor']= ft_background
    plt.rcParams['text.color']= ft_maybegrey
    plt.rcParams['xtick.color']= ft_maybegrey
    plt.rcParams['ytick.color']= ft_maybegrey
    plt.rcParams['axes.labelcolor']= ft_maybegrey

    plt.rcParams["axes.grid.axis"] ="y"
    plt.rcParams["axes.grid"] = True
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = True
    plt.rcParams['figure.figsize'] = (18,10)

    plt.rcParams['axes.titlesize'] = largefont
    plt.rcParams['font.size'] = smallfont
    plt.rcParams['xtick.labelsize'] = tinyfont
    plt.rcParams['ytick.labelsize'] = tinyfont
    plt.rcParams['axes.labelsize']  = smallfont    
    plt.rcParams['xtick.major.size'] = 10
    plt.rcParams['xtick.major.pad'] = 10
    plt.rcParams['ytick.major.size'] = 0
    plt.rcParams['ytick.major.pad'] = 10


    plt.rcParams['lines.linewidth'] = linewidth
    plt.rc('axes', prop_cycle=(cycler('color', [ft_darkblue, ft_blue, ft_lightblue, ft_pink, ft_darkred, ft_greenish])))

    return None
