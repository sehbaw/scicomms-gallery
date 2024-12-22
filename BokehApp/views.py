'''import bokeh
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure, show 
#from bokeh.embed import components4

#other libraries
from numpy.random import standard_normal
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from bokeh.models import LogColorMapper

# Create your views here.
#this is the file where you can actually make your graphs!!!!

def home(request): # want to make a 3x3 grid 
#better to store it in plot to easily wrap in the components
 ##### first row
 ##
 
    # first graph
    plot = figure(plot_width=600, plot_height=600)


# second graph
x = standard_normal (50000)
y = standard_normal(5000)

bins = hexbin(x,y,0.1)
p = figure(tools='', match_aspect=True, background_fill_color='8000080')
p.grid.visible = False

p.hex_tile(q='q', r='r', size=0.1, line_color=None, source=bins, 
           fill_color=linear_cmap('counts', 'Plasma')) #wanna change out the colormaps'''

# third graph
''' def normal2d(X,Y, sigx=1.0, sigy=1.0, mux=0.0, muy=0.0):
        z=(x-mux)**2 / sigx**2 + (Y-muy)**2 / sigy**2
        return np.exp(-z/2) / (2*np.pi * sigx * sigy)
X, Y = np.mgrid[-3,3:200j, -2:2:200j]
Z = normal2d(X, Y, 0.1,0.2,1.0,1.0) + 0.1* normal2d(X,Y, 1.0, 1.0)
image = Z
  #GnBu'''

from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap, factor_mark
from bokeh.embed import components
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.layouts import gridplot


from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure



import numpy as np

from bokeh.models import LogColorMapper
from bokeh.plotting import figure, show



from numpy.random import standard_normal

from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

from bokeh.layouts import gridplot

def home(request):
        from bokeh.layouts import row
        from bokeh.plotting import figure, show

        x = list(range(11))
        y0 = x
        y1 = [10 - i for i in x]
        y2 = [abs(i - 5) for i in x]

        # create three plots
        s1 = figure(width=250, height=250, background_fill_color="#fafafa")
        s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

        s2 = figure(width=250, height=250, background_fill_color="#fafafa")
        s2.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

        s3 = figure(width=250, height=250, background_fill_color="#fafafa")
        s3.square(x, y2, size=12, color="#d95b43", alpha=0.8)

        # put the results in a row and show
#row2   
        s4 = figure(width=250, height=250, background_fill_color="#fafafa")
        s4.circle(x, y0, size=12, color="#53777a", alpha=0.8)

        s5 = figure(width=250, height=250, background_fill_color="#fafafa")
        s5.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

        s6 = figure(width=250, height=250, background_fill_color="#fafafa")
        s6.square(x, y2, size=12, color="#d95b43", alpha=0.8)
#row3
        s7 = figure(width=250, height=250, background_fill_color="#fafafa")
        s7.square(x, y2, size=12, color="#d95b43", alpha=0.8)
#
       # s7 = figure(width=250, height=250, background_fill_color="#fafafa")
      #  s7.circle(x, y0, size=12, color="#53777a", alpha=0.8)

        #s8 = figure(width=250, height=250, background_fill_color="#fafafa")
        #s8.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

       # s9 = figure(width=250, height=250, background_fill_color="#fafafa")
      #  s9.square(x, y2, size=12, color="#d95b43", alpha=0.8)

       # grid = gridplot([s1,s2,s3,s4,s5,s6,s7,s8,s9])
        #grid = show(gridplot([s1,s2,s3]))
        grid1 = gridplot([[s1,s2,s3], [s4,s5,s6,s7]])
        #script, div = components(grid)
        script, div = components(grid1)

   
        #div1 = script


        # put the results in a row and show
       # show(row(s1, s2, s3))
       
        #plots_1 = row(s1,s2,s3)
        #plots_2 = row(s4,s5,s6) 
        #plots_3 = row(s7,s8,s9)
        #script, div = components(plots_1,plots_2, plots_3)
        ##div1 = plots_1
        #div2 = plots_2
        #div3 = plots_3
        context = {
                'script': script,
                'div': div
        }

        return render(request, 'base.html', context=context)