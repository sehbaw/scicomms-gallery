import holoviews as hv
import numpy as np 
import pandas as pd
hv.extension('bokeh')
#non-bokeh
from random import random 
from itertools import combinations


#plotting 
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap, factor_mark
from bokeh.embed import components
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.models import ColumnDataSource, FixedTicker
from bokeh.models import Whisker
from bokeh.sampledata.autompg2 import autompg2 as df
from bokeh.transform import factor_cmap, jitter
from bokeh.palettes import GnBu3, OrRd3 #saying that something is wrong with this?
from bokeh.layouts import column
from bokeh.plotting import figure
import numpy as np
from bokeh.models import LogColorMapper
from numpy.random import standard_normal
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from bokeh.layouts import gridplot
from bokeh.layouts import row
#models 
from bokeh.models import Label, PrintfTickFormatter
from bokeh.models import CrosshairTool, Span

from sklearn.neighbors import KernelDensity
#other 
from bokeh.palettes import Dark2_5 as colors
from bokeh.sampledata.cows import data as df
from bokeh.layouts import column





import numpy as np
import holoviews as hv
from holoviews import opts

hv.extension('bokeh')

#data 
df_rain = pd.read_csv('\BokehDjango\scicomms-gallery\BokehDjango\data\weatherAUS.csv')
df_rain = 




def home(request):

#figure 2 

        x = [random() * 15 for _ in range(100)]
        y = [random() * 15 for _ in range(100)]
        width = Span(dimension="width", line_dash="dashed", line_width=2)
        height = Span(dimension='height', line_dash='dotted', line_width=2)

        s2 = figure(height=400, width=400, x_range=(0,15), y_range=(0,15), tools="hover", toolbar_location=None)
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

        s5 = figure(y_range=fruits, height=400, x_range=(-15,15), title="Fruit import/export by year", toolbar_location=None)
        s5.hbar_stack(years, y="fruits", height=0.9, color=OrRd3, source=ColumnDataSource(exports), 
                legend_label=['f {year} imports' for year in years])
        s5.hbar_stack(years, y="fruits", height=0.9, color=OrRd3, source=ColumnDataSource(imports), 
                        legend_label=['f {year} imports' for year in years])
        s5.y_range.range_padding = 0.1
        s5.ygrid.grid_line_color = None
        s5.legend.location = "top_left"
        s5.axis.minor_tick_line_color = None
        s5.outline_line_color = None


        source = ColumnDataSource(df_rain)
        s6 = figure(height=400, width=400,x_range='Sunshine',y_range='Rainfall[mm]', toolbar_location='above', toolbar_sticky=False)
        s6.circle(x="Sunshine", y="Rainfall",
                  source=source, color='F7999',)
        s6.title.text_font_size = '20pt'
        s6.title.text_font_style = 'bold'
        s6.title.text_font = 'Serif'
        s6.xaxis.axis_label_text_font_size = '16pt'
        s6.yaxis.axis_label_text_font_size = '16pt'
#row 2 
               



#row3


        #grid1 = gridplot([[s1,s4,s5], [s6, s7]])
        #script, div = components(grid)
        grid1 = gridplot([[s4,s5, s6]])
        script, div = components(grid1)

        context = {
                'script': script,
                'div': div
        }

        return render(request, 'base.html', context=context)




#row2   
'''     classes = list(sorted(df['class'].unique()))
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

                )'''
      
#row3
    
'''xvals = [0.1* i for i in range(100)]
        curve =  hv.Curve((xvals, [np.sin(x) for x in xvals]))
        scatter =  hv.Scatter((xvals[::5], np.linspace(0,1,20)))
        scatter1 =  hv.Scatter((xvals[::5], np.linspace(0,1,20)))

        from holoviews.plotting.links import DataLink

        scatter1 = hv.Scatter(np.arange(100))
        scatter2 = hv.Scatter(np.arange(100)[::-1], 'x2', 'y2')

        dlink = DataLink(scatter1, scatter2)

        (scatter1 + scatter2).opts(
                 opts.Scatter(tools=['box_select', 'lasso_select']))'''
   