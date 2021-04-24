import random
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
result = []
count = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result.append(dice1+dice2)
   # print(result)
    count.append(i)
fig = px.bar(x=result, y=count)
fig = ff.create_distplot([result], ["Result"],
                         curve_type="kde", show_hist=False)
# fig.show()

mean = statistics.mean(result)
median = statistics.median(result)
mode = statistics.mode(result)
std = statistics.stdev(result)
print("mean by statistics: ", + mean)
print("median by statistics: ", + median)
print("mode by statistics: ", + mode)
print("standard deviation by statistics: ", + std)

first_start, first_end = mean-std, mean+std
second_start, second_end = mean - (2*std), mean+(2*std)
third_start, third_end = mean-(3*std), mean+(3*std)

print("first : ", +first_start, + first_end)
print("second : ", +second_start, + second_end)
print("third : ", +third_start, + third_end)

list_of_data_witin_1st_stddev = [
    res for res in result if res > first_start and res < first_end]
# print(list_of_data_witin_1st_stddev)
list_of_data_witin_2nd_stddev = [
    res for res in result if res > second_start and res < second_end]
# print(list_of_data_witin_2nd_stddev)
list_of_data_witin_3rd_stddev = [
    res for res in result if res > third_start and res < third_end]
# print(list_of_data_witin_3rd_stddev)

print("{}% of data lies within 1 standard deviation".format(
    len(list_of_data_witin_1st_stddev)*100.0/len(result)))
print("{}% of data lies within 2 standard deviations".format(
    len(list_of_data_witin_2nd_stddev)*100.0/len(result)))
print("{}% of data lies within 3 standard deviations".format(
    len(list_of_data_witin_3rd_stddev)*100.0/len(result)))

fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_start, first_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1 start"))
fig.add_trace(go.Scatter(x=[first_end, first_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1 end"))
fig.add_trace(go.Scatter(x=[second_start, second_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_end, second_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()
