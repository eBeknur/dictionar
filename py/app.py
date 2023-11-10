# importing pygal
import pygal
# creating pie_chart object
pie_chart = pygal.Pie()
pie_chart.title = 'statistika'
# adding random data
pie_chart.add('A', 20.5)
pie_chart.add('B', 36.0)
pie_chart.add('C', 35.9)
pie_chart.add('D', 5.5)
pie_chart.add('E', 1.3)
# rendering the svg to the file
pie_chart.render_to_file('pie_chart.svg')