# %% [markdown]
# # Чаевые в ресторане

# %% [markdown]
# Это задание основано на туториале Seaborn. Используйте здесь эту библиотеку.
# Документация - https://seaborn.pydata.org/index.html
# Памятка по выбору графика в seaborn - https://martinnormark.com/a-simple-cheat-sheet-for-seaborn-data-visualization-2/
#
#
# ### Шаг 1. Импортируем библиотеки

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import streamlit as st


# %%

# Шаг 2. Указываем заголовок страницы.
st.write(
    """
# WEB-приложение для анализа датасета tips.csv.

Источник данных: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
"""
)

# %% [markdown]
# ### Шаг 3. Прочитаем датасет в переменную `tips`

# %%
path = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
# path = '../learning/datasets/tips.csv'


# %%
tips = pd.read_csv(path)

# tips

# %% [markdown]
# ### Шаг 4. Создаем столбец `time_order`
# ### Заполняем его случайной датой в промежутке от 2023-01-01 до 2023-01-31

# %%
start_date = "2023-01-01"
end_date = "2023-01-31"
num_rows = len(tips["total_bill"])

tips["time_order"] = pd.to_datetime(
    np.random.choice(pd.date_range(start=start_date, end=end_date), num_rows)
)

# tips.head(5)

# %%
# tips.to_excel("tips.xlsx")

# %% [markdown]
# ### Шаг 5. Построим график показывающий динамику чаевых во времени

# %%
# Copy df and sort it
sorted_tips = tips.sort_values("time_order")
sorted_mean_tips = (
    sorted_tips.groupby(pd.Grouper(key="time_order", freq="D"))
    .agg(mean_tips=("tip", "mean"))
    .reset_index()
)
sorted_mean_tips["mean_tips"] = sorted_mean_tips["mean_tips"].round(2)

# plt.style.use('ggplot')
sns.set_style("whitegrid")

fig = plt.figure(figsize=(8, 4))


sns.lineplot(
    data=sorted_tips,
    x="time_order",
    y="tip",
    errorbar=("ci", 100),
    label="Tips",
)

plt.title("Tips per day", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Tips", fontsize=12)
plt.xticks(sorted_tips["time_order"], rotation=90)
plt.xlim(pd.Timestamp("2023-01-01"), pd.Timestamp("2023-01-31"))
plt.ylim(0, 11)
plt.legend()

st.write("### Таблица с исходными данными")
st.write(sorted_tips)


st.write("### График, показывающий динамику чаевых во времени (тип seaborn lineplot)")
st.pyplot(fig)

st.write("### Средние чаевые")
st.write(sorted_mean_tips)

st.write("#### Интерактивная версия линейного графика", unsafe_allow_html=True)
st.line_chart(
    sorted_mean_tips,
    x="time_order",
    y="mean_tips",
    color=["#FF0000"],
    use_container_width=True,
)

st.write("#### Интерактивная версия графика типа scatter_chart", unsafe_allow_html=True)
st.scatter_chart(
    sorted_tips,
    x="time_order",
    y="tip",
    color=["#FF0000"],
    size=30,
    use_container_width=True,
)

# %% [markdown]
# Сделаем аналогичный график используя многофункциональный метод [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html)

# %%
# Copy df and sort it
sorted_tips = tips.sort_values("time_order")

# plt.style.use('ggplot')
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.relplot(
    data=sorted_tips, x="time_order", y="tip", label="Tips", height=4, aspect=2.5
)
plt.title("Tips per day", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Tips", fontsize=12)
plt.xticks(sorted_tips["time_order"], rotation=90)
plt.xlim(pd.Timestamp("2022-12-31"), pd.Timestamp("2023-02-01"))
plt.legend()

# plt.show()

st.write("### График, показывающий динамику чаевых во времени (тип seaborn replot)")
st.pyplot(fig)


# %% [markdown]
# ### Шаг 5. Нарисуем гистограмму `total_bill`

# %%
# Copy df and sort it
sorted_tips = tips.sort_values("total_bill")

sorted_tips.head(15)

# %%
# plt.style.use('ggplot')
sns.set_style("whitegrid")

plt.figure(figsize=(12, 4))

sns.histplot(
    data=sorted_tips, x="total_bill", bins=55, binwidth=1, kde=True, label="Bills"
)
plt.title("Number of bills", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Number", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.yticks(range(0, 19, 1), rotation=0)
plt.xlim(0, 55)
plt.ylim(0, 20)
plt.legend()

# plt.show()

st.write(
    "### График, показывающий распределение сумм общего счета (тип seaborn histplot)"
)
st.pyplot(fig)


# %% [markdown]
# Сделаем аналогичный график, используя многофункциональный метод [displot](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot)
# Используем другие формы отображения меняя параметр параметр `kind`

# %%
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.displot(
    data=sorted_tips,
    x="total_bill",
    kind="hist",
    bins=55,
    kde=True,
    height=4,
    aspect=2.55,
    label="Bills",
)
plt.title("Number of bills", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Number", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.yticks(range(0, 19, 1), rotation=0)
plt.xlim(0, 55)
plt.ylim(0, 20)
plt.legend()

# plt.show()

st.write(
    "### График, показывающий распределение сумм общего счета (тип seaborn displot, kind='hist')"
)
st.pyplot(fig)


# %%
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.displot(
    data=sorted_tips, x="total_bill", kind="ecdf", height=4, aspect=2.5, label="Bills"
)
plt.title("Number of bills", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Number", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.xlim(0, 55)
plt.legend()

# plt.show()

st.write(
    "### График, показывающий распределение сумм общего счета (тип seaborn displot, kind='ecdf')"
)
st.pyplot(fig)

# %%
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.displot(
    data=sorted_tips, x="total_bill", kind="kde", height=4, aspect=2.5, label="Bills"
)
plt.title("Number of bills", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Number", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.xlim(0, 55)
plt.legend()

# plt.show()

st.write(
    "### График, показывающий распределение сумм общего счета (тип seaborn displot, kind='kde')"
)
st.pyplot(fig)

# %% [markdown]
# ### Шаг 6. Нарисуем scatterplot, показывающий связь между `total_bill` and `tip`

# %%
sns.set_style("whitegrid")

fig = plt.figure(figsize=(12, 4))

sns.scatterplot(data=sorted_tips, x="total_bill", y="tip", size=sorted_tips["tip"])
plt.title("Relationships between total bill and tips", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Tips, $", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.yticks(range(0, 13, 1), rotation=0)
plt.xlim(0, 55)
plt.ylim(0, 12)
# plt.legend()

# plt.shew()

st.write(
    "### График, показывающий связь между `total_bill` and `tip` (тип seaborn scatterplot)"
)
st.pyplot(fig)

st.write("#### Интерактивная версия графика типа scatter_chart", unsafe_allow_html=True)
st.scatter_chart(
    sorted_tips,
    x="total_bill",
    y="tip",
    color=["#FF0000"],
    size="tip",
    use_container_width=True,
)

# %% [markdown]
# Сделаем аналогичный график, используя многофункциональный метод [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html)

# %%
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.relplot(
    data=sorted_tips,
    x="total_bill",
    y="tip",
    size=sorted_tips["tip"],
    height=4,
    aspect=2.3,
)
plt.title("Relationships between total bill and tips", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Tips, $", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.yticks(range(0, 13, 1), rotation=0)
plt.xlim(0, 55)
plt.ylim(0, 12)
# plt.legend()

# plt.show()

st.write(
    "### График, показывающий связь между `total_bill` and `tip` (тип seaborn relplot)"
)
st.pyplot(fig)

# %% [markdown]
# ### Шаг 7. Нарисуем 1 график, связывающий `total_bill`, `tip`, и `size`
# #### Подсказка: это одна функция

# %%
sns.set_style("whitegrid")

# plt.figure(figsize=(12,4))

fig = sns.relplot(
    data=sorted_tips,
    x="total_bill",
    y="tip",
    size=sorted_tips["size"],
    height=4,
    aspect=2.3,
)
plt.title("Relationships between total bill and tips", fontsize=16)
plt.xlabel("Total bill, $", fontsize=12)
plt.ylabel("Tips, $", fontsize=12)
plt.xticks(range(0, 56, 1), rotation=0)
plt.yticks(range(0, 13, 1), rotation=0)
plt.xlim(0, 55)
plt.ylim(0, 12)

# plt.show()

st.write(
    "### График, показывающий связь между `total_bill`, `tip` и  size` (тип seaborn relplot)"
)
st.pyplot(fig)

# %% [markdown]
# ### Шаг 8. Покажим связь между днем недели и размером счета

# %%
# Copy df and sort it and then filter
sorted_tips = tips.sort_values("time_order")

sorted_tips["week_day"] = sorted_tips["time_order"].dt.day_name()
sorted_tips["week_day_number"] = sorted_tips["time_order"].dt.day_of_week
sorted_tips = (
    sorted_tips.groupby(by=["week_day", "week_day_number"])["total_bill"]
    .sum()
    .reset_index()
)
sorted_tips = sorted_tips.sort_values("week_day_number")

sorted_tips


# %%
# plt.style.use('ggplot')
sns.set_style("whitegrid")

fig = plt.figure(figsize=(8, 4))

sns.lineplot(
    data=sorted_tips, x="week_day", y="total_bill", errorbar=("ci", 100), label="Bill"
)
plt.title("Bills per day of week", fontsize=16)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Summary bills", fontsize=12)
plt.xticks(sorted_tips["week_day"])
plt.legend()

# plt.show()

st.write(
    "### График, показывающий связь между днем недели и размером счета (тип seaborn lineplot)"
)
st.pyplot(fig)

st.write("#### Интерактивная версия линейного графика")
st.line_chart(
    sorted_tips,
    x="week_day",
    y="total_bill",
    color=["#FF0000"],
    use_container_width=True,
)


# %%
# Copy df and sort it and then filter
sorted_tips = tips.sort_values("time_order")

sorted_tips["week_day"] = sorted_tips["time_order"].dt.day_name()
sorted_tips["week_day_number"] = sorted_tips["time_order"].dt.day_of_week
sorted_tips = sorted_tips.sort_values("week_day_number")

sorted_tips

# %%
sns.set_style("whitegrid")

fig = sns.relplot(
    data=sorted_tips, x="week_day", y="total_bill", label="Bill", height=5, aspect=2.0
)
plt.title("Bills per day of week", fontsize=16)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Bills", fontsize=12)
plt.xticks(sorted_tips["week_day"], rotation=0)
# plt.xlim(pd.Timestamp('2022-12-31'),pd.Timestamp('2023-02-01'))
plt.legend()

# plt.show()

st.write(
    "### График, показывающий связь между днем недели и размером счета (тип seaborn relplot)"
)
st.pyplot(fig)


# %% [markdown]
# ### Шаг 9. Нарисуем `scatter plot` с днем недели по оси **Y**, чаевыми по оси **X**, и цветом по полу

# %%
# Copy df and sort it and then filter
sorted_tips = tips.sort_values("time_order")

sorted_tips["week_day"] = sorted_tips["time_order"].dt.day_name()
sorted_tips["week_day_number"] = sorted_tips["time_order"].dt.day_of_week
sorted_tips = sorted_tips.sort_values("week_day_number")

sorted_tips

# %%
sns.set_style("whitegrid")

fig = plt.figure(figsize=(12, 4))

sns.scatterplot(data=sorted_tips, x="tip", y="week_day", hue="sex")
plt.title("Relationships between days of week, tips and sex", fontsize=16)
plt.xlabel("Tips, $", fontsize=12)
plt.ylabel("Days of week", fontsize=12)

# plt.show()

st.write(
    "### График, показывающий связь между днем недели (ось Y) и размером чаевых (ось Х) (тип seaborn scatterplot)"
)
st.pyplot(fig)

st.write("#### Интерактивная версия графика типа scatter_chart")
st.scatter_chart(
    sorted_tips,
    x="tip",
    y="week_day",
    color="sex",
    use_container_width=True,
)


# %% [markdown]
# ### Шаг 10. Нарисуем `box plot` c суммой всех счетов за каждый день, разбивая по `time` (Dinner/Lunch)
#
# Как понимать boxplot? https://tidydata.ru/boxplot

# %%
# Copy df and sort it
sorted_tips = tips.sort_values("time_order")

# sorted_tips = sorted_tips.groupby(by=['time_order', 'time'])['total_bill'].sum().reset_index()

sorted_tips.head(10)

# %%
sns.set(style="whitegrid")

fig = plt.figure(figsize=(12, 6))
sns.boxplot(
    data=sorted_tips, x="time_order", y="total_bill", hue="time", palette="Set2"
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot)"
)
st.pyplot(fig)

# %% [markdown]
# Пострем аналогичный график, используя многофункциональный метод [catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot)
# Применим другие формы отображения графика, меняя параметр параметр `kind`

# %%
# kind='strip'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="strip",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='strip')"
)
st.pyplot(fig)

# %%
# kind='swarm'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="swarm",
    s=21,
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='swarm')"
)
st.pyplot(fig)

# %%
# kind='box'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="box",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='box')"
)
st.pyplot(fig)

# %%
# kind='violin'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="violin",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(-25, 85, 5), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='violin')"
)
st.pyplot(fig)


# %%
# kind='boxen'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="boxen",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='boxen')"
)
st.pyplot(fig)


# %%
# kind='point'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="point",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='point')"
)
st.pyplot(fig)

# %%
# kind='bar'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    y="total_bill",
    hue="time",
    kind="bar",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Total Bill by Day and Time")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total bills, $", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 55, 2), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='bar')"
)
st.pyplot(fig)

# %%
# kind='count'

sns.set(style="whitegrid")

# plt.figure(figsize=(12, 6))
fig = sns.catplot(
    data=sorted_tips,
    x="time_order",
    hue="time",
    kind="count",
    palette="Set2",
    height=5,
    aspect=2,
)
plt.title("Dinner & Lunch number per day")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Dinner & Lunch number", fontsize=12)
plt.xticks(rotation=90)
plt.yticks(range(0, 14, 1), rotation=0)

# plt.show()

st.write(
    "### График, показывающий сумму всех счетов за каждый день с разбивкой по Dinner/Lunch (тип seaborn boxplot, kind='count')"
)
st.pyplot(fig)

st.write(
    "#### Интерактивная версия графика типа bar_chart, показывающая сумму счетов по дням с разбивкой на обед и ужин"
)
st.bar_chart(
    sorted_tips,
    x="time_order",
    y="total_bill",
    color="time",
    use_container_width=True,
)

# %% [markdown]
# ### Шаг 11. Нарисуем 2 гистограммы чаевых на обед и ланч. Расположим их рядом по горизонтали.

# %%
# В описании задания ошибка: вместо "обед и ланч" надо написать "обед и ужин"

# Create two df by copying df tips and filtering it by time, then sort it by date
sorted_tips_lunch = tips[tips["time"] == "Lunch"].sort_values("time_order")

sorted_tips_dinner = tips[tips["time"] == "Dinner"].sort_values("time_order")

# %%
# Plot a draw
sns.set_style("whitegrid")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 1st histogram
sns.histplot(
    data=sorted_tips_lunch,
    x="tip",
    ax=ax1,
    bins=12,
    binwidth=1,
    kde=True,
    label="Tips",
    color="orange",
)
ax1.set_title("Number of tips during lunch", fontsize=16)
ax1.set_xlabel("Tips, $", fontsize=12)
ax1.set_ylabel("Number", fontsize=12)
ax1.set_xticks(range(0, 15, 1))
# ax1.set_yticks(range(0, 30))
ax1.set_xlim(0, 15)
# ax1.set_ylim(0,30)
ax1.legend()

# 2nd histogram
sns.histplot(
    data=sorted_tips_dinner,
    x="tip",
    ax=ax2,
    bins=12,
    binwidth=1,
    kde=True,
    label="Tips",
    color="darkblue",
)
ax2.set_title("Number of tips during dinners", fontsize=16)
ax2.set_xlabel("Tips, $", fontsize=12)
ax2.set_ylabel("Number", fontsize=12)
ax2.set_xticks(range(0, 15, 1))
# ax2.set_yticks(range(0, 30))
ax2.set_xlim(0, 15)
# ax2.set_ylim(0,30)
ax2.legend()

# plt.tight_layout()
# plt.show()

st.write("### График распределения чаевых на обед и ужин (тип seaborn histplot)")
st.pyplot(fig)

# %% [markdown]
# ### Шаг 12. Нарисуем 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.

# %%
# Create two df by copying df tips and filtering it by sex, then sort it by date
tips_men = tips[tips["sex"] == "Male"].sort_values("time_order")

tips_women = tips[tips["sex"] == "Female"].sort_values("time_order")

# %%
# Plot a draw
sns.set_style("whitegrid")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 1st scatterplot
sns.scatterplot(data=tips_men, ax=ax1, x="total_bill", y="tip", hue="smoker")
ax1.set_title(
    "Relationships between bill and tips\nfor smoking and non-smoking men", fontsize=16
)
ax1.set_xlabel("Total bill, $", fontsize=12)
ax1.set_ylabel("Tips, $", fontsize=12)
ax1.set_xticks(range(0, 55, 2))
ax1.set_yticks(range(0, 12, 1))

# 2nd scatterplot
sns.scatterplot(data=tips_women, ax=ax2, x="total_bill", y="tip", hue="smoker")
ax2.set_title(
    "Relationships between bill and tips\nfor smoking and non-smoking women",
    fontsize=16,
)
ax2.set_xlabel("Total bill, $", fontsize=12)
ax2.set_ylabel("Tips, $", fontsize=12)
ax2.set_xticks(range(0, 55, 2))
ax2.set_yticks(range(0, 12, 1))

plt.tight_layout()
# plt.show()

st.write(
    "### Графики по мужчинам и женщинам, показывающие связь между счетом и чаевыми с разбивкой на курящих/не курящих (тип seaborn scatterplot)"
)
st.pyplot(fig)

# %% [markdown]
# ### Шаг 13. Построим тепловую карту зависимостей численных переменных
# Матрица корреляций в pandas - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

# %%
# Copy df and sort it
sorted_tips = tips.sort_values("time_order")

# Build correlation corr_matrix
corr_matrix = sorted_tips.corr(numeric_only=True)

corr_matrix

# %%
fig.clear()
fig = plt.figure(figsize=(9, 8))
# Plot a heatmap
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    xticklabels=["Total bills", "Tips", "Size"],
    yticklabels=["Total bills", "Tips", "Size"],
)
plt.title("Heatmap of numerical variables")

# plt.show()

# Save the heatmap as an image
plt.savefig("heatmap.png")

st.write("### Тепловая карта зависимостей численных переменных (тип seaborn heatmap)")
st.image("heatmap.png")
