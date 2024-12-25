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
from bokeh.models import ColumnDataSource
from bokeh.models import Whisker
from bokeh.sampledata.autompg2 import autompg2 as df
from bokeh.transform import factor_cmap, jitter
from bokeh.plotting import GnBu3, OrRd3
#from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure
import numpy as np
from bokeh.models import LogColorMapper
from numpy.random import standard_normal
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from bokeh.layouts import gridplot
from bokeh.layouts import row

from random import random 
from bokeh.models import CrosshairTool, Span

from sklearn.neighbors import KernelDensity

from bokeh.models import Label, PrintfTickFormatter
from bokeh.palettes import Dark2_5 as colors
from bokeh.sampledata.cows import data as df




def home(request):

#figure 1 
        def normal2d(X,Y, sigx=1.0, sigy=1.0, mux=0.0, muy=0.0):
                        z = (X-mux**2 + (Y-muy **2 / sigy**2))
                        return np.exp(-z/2) / 92*np.pi * sigx * sigy)
        X,Y = np.mgrid[-3:3:200j, -2:2:200j]
        Z = normal2d(X,Y,0.1,0.2,1.0,1.0)+ 0.1*normal2d(X,Y,1.0,1.0)
        image = Z * 1e6
        color_mapper = LogColorMapper(palette="Viridis256", low=1, high=1e7)
        s1 =figure(x_range(0,1), y_range=(0,1), toolbar_location=None)
        r = s1.image(image=[image], color_mapper=color_mapper, dh=1.0, dw=1.0, x=0,y=0)
        color_bar = r.construct_color_bar(padding=2)
        s1.add_layout(color_bar, "right")

#figure 2 

        x = [random() * 15 for _ in range(100)]
        y = [random() * 15 for _ in range(100)]
        width = Span(dimension="width", line_dash="dashed", line_width=2)
        height = Span(dimension='height', line_dash='dotted', line_width=2)

        s2 = figure(height=400, height=400, x_range=(0,15), y_range=(0,15), tools="hover", toolbar_location="None")
        s2.add_tools(CrosshairTool(overlay=[width, height]))
        s2.circle(x,y,radius=0.2, alpha=0.3, hover_alpha=1.0)

        s3 = figure(height=400, width=200, x_range=(0,5), y_range=(0,5), tools="hover", toolbar_location=None)
        s3.circle(x,y, radius=0.2, alpha=0.3, hover_alpha=1.0)

        s4 = row(s2,s3)

        #figure 3 
        fruits = ["apples", "pears", "nectarines", "plums", "grapes", "strawberries"]
        years = ["2015", "2016", "2017"]
        exports = {
                'fruits': fruits, 
                "2015": [2,1,3,5,1],
                "2016" : [1,4,5,6,3,2],
                "2017" : [2,3,4,5,6,1]
        }
        imports = {
                'fruits': fruits, 
                "2015": [-1,-4,-5,-1,0],
                "2016": [0,-3,-5,-1,-2],
                "2017" : [-1,-4,0,-2,-1]
        }

        s5 = figure(y_range=fruits, height=350, x_range=(-15,15), title="Fruit import/export by year", toolbar_location=None)
        s5.hbar_stack(years, y="fruits", height=0.9, color=OrRd3, source=ColumnDataSource(exports), 
                legend_label=['f {year} imports' for year in years])
        s5.hbar_stack(years, y="fruits", height=0.9, color=OrRd3, source=ColumnDataSource(imports), 
                        legend_label=['f {year} imports' for year in years])
        s5.y_range.range_padding = 0.1
        s5.ygrid.grid_line_color = None
        s5.legend.location = "top_left"
        s5.axis.minor_tick_line_color = None
        s5.outline_line_color = None



#row2   
        classes = list(sorted(df['class'].unique()))
        s6 = figure(height=400, x_range=classes, background_fill_color='#efefef', 
                    title="Car class vs HWY mpg with quantile ranges")
        s6.xgrid.grid_line_color = None

        group = df.groupby("class")
        upper = g.hwy.quantile(0.80)
        lower = g.hwy.quantile(0.20)
        source = ColumnDataSource(data=dict(base=classes, upper=upper, lower=lower))

        error = Whisker(base="base", upper="upper", source=source, level='annotation', line_width=2)

        error.upper_head.size = 20
        error.lower_head.size=20
        s6.add_layout(error)

        s6.scatter(jitter('class', 0.3, range=p.x_range,), "hwy", source=df, alpha=0.5, size=13, line_color="white", color=factor_cmap('class', "Light7", classes))
#figure
        s7 = figure(width=400, height=400)
        s7.varea(x=[1,3,5,7,9],
                 y1=[2,4,6,8,10],
                y2=[5,10,15,20,25])
#figgure 
        breed_groups = df.groupby('breed')
        x = np.linspace(2,8,1000)
        source = ColumnDataSource(dict(x=x))

        s8 = figure(title="Denisty estimates", height=300, x_range=(2.5,7.5), x_axis_label="butterfat contents")

        for (breed, breed_df), color in zip(breed_groups, colors):
                data = breed_df['butterfat'].values
                kde= KernelDensity(kernel='gaussian', bandwidth=0.2).fit(data[:, np.newaxis])
                log_density = kde.score_sample(x[:, np.newaxis])
                y = np.exp(log_density)
                source.add(y, breed)
                s8.varea(x='x',y1=breed, y2=0,source=source, fill_alpha=0.3, fill_color=color)

                max_idx = np.argmax(y),
                highest_point_label=Label(
                        x=x[max_idx],
                        y=y[max_idx],
                        text=breed,
                        text_font_size='10pt',
                        x_offset=10, 
                        y_offset=-5,
                        text_color=color,

                )
        

#row3
   
#
       # s7 = figure(width=250, height=250, background_fill_color="#fafafa")
      #  s7.circle(x, y0, size=12, color="#53777a", alpha=0.8)

        #s8 = figure(width=250, height=250, background_fill_color="#fafafa")
        #s8.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

       # s9 = figure(width=250, height=250, background_fill_color="#fafafa")
      #  s9.square(x, y2, size=12, color="#d95b43", alpha=0.8)

       # grid = gridplot([s1,s2,s3,s4,s5,s6,s7,s8,s9])
        #grid = show(gridplot([s1,s2,s3]))
        grid1 = gridplot([[s1,s4,s5], [s6, s7]])
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