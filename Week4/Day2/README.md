# Week 4, Day 2 – Daily Challenge: Global Power Plant Database

Notebook: [`challenge.ipynb`](challenge.ipynb) · Exercises XP: [`exercisexp.ipynb`](exercisexp.ipynb)

Dataset: World Resources Institute, *Global Power Plant Database* v1.3 (`global_power_plant_database.csv`).

**How the libraries were used:** NumPy for type conversion, statistics per fuel type, boolean filtering (`np.isin`, `np.select`), log-spaced histogram bins and the correlation/eigen analysis (`np.linalg.eigh`); Pandas for cleaning, grouping and pivot tables; SciPy for ANOVA, Kruskal-Wallis and a Welch t-test; Matplotlib and Seaborn for the map, bar charts, box plots and stacked bars.

## Key insights
1. **Scale:** ~35,000 plants in 167 countries, with a total capacity of about **5.7 million MW**. China (~1.4M MW) and the USA (~1.2M MW) together hold almost half of it; the USA has by far the most *plants* (~9,800), but many are small.
2. **Many plants ≠ much power:** Solar is the most common plant type (10,665 plants) but only **3.3%** of capacity, because most solar plants are tiny (median 5.8 MW). **Coal (34%) and gas (26%)** still dominate installed capacity, followed by hydro (19%).
3. **Very different plant sizes:** nuclear plants are the biggest on average (median ~1,900 MW), then coal (600 MW). The largest single plant is China's Three Gorges Dam (22,500 MW, hydro). Capacity is extremely skewed, so medians and log scales are needed to compare fuels.
4. **Statistics:** ANOVA and Kruskal-Wallis both give p ≈ 0, and coal vs. gas (Welch t-test) p ≈ 10⁻¹⁰⁹: **mean capacity differs significantly between fuel types**.
5. **The fuel mix over time:** hydro was ~47% of new capacity in the 1950s and fell to ~9–12% by the 2000s–2010s. Coal was the largest share of new capacity from the 1970s to the 2010s (~40–50%), and nuclear peaked in the 1970s–80s (~11–19%). From the 2010s, **wind and solar grew fast**, and in the (small, ~150-plant) 2020 sample they make up ~75% of new capacity.
6. **Geography:** the map shows dense clusters in the USA, Europe, India and East Asia, with large coal plants concentrated in Asia, and many small solar/wind plants in Europe and the USA.
7. **Matrix analysis:** capacity and generation are almost perfectly correlated (r = 0.96, on log scale). The first eigenvector, a "plant size" factor (capacity + generation + being fossil-fuelled), explains ~43% of the variance; the second mainly contrasts latitude with commissioning year. One eigenvalue is close to 0 (0.04), showing that capacity and generation carry nearly the same information.
8. **New large renewables:** of the 52 renewable plants over 500 MW commissioned after 2010, about half are in **China**.

**Data caveats:** commissioning year is missing for half the plants, so the time analysis covers only the plants where it's known; the 2020 "decade" has very few plants; and generation figures for 2017 are estimates.
