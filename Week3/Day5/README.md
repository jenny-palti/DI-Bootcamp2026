# Week 3, Day 5 – US Superstore analysis

Dataset: US Superstore (9,994 order lines, Jan 2014 – Dec 2017, United States only).
The csv file is in `../Day4/superstore_dataset.csv`.

## Files
- `miniproject.ipynb` – Mini-Project: Data Analysis for Marketing Strategy (states, cities, customers, Pareto).
- `challenge.ipynb` – Daily Challenge: Interactive Data Visualization with Matplotlib and Seaborn.

> The interactive line chart (`ipywidgets`) and the interactive map (`plotly`) need a live notebook, so their outputs are not saved in the file. Run those two cells in Jupyter or Google Colab.

## Key insights – Daily Challenge
1. **Growth:** sales fell slightly in 2015 (-2.8%), then grew +29.5% in 2016 and +20.4% in 2017 ($484k in 2014 to $733k in 2017). Profit went from about $49.5k to $93.4k.
2. **Seasonality:** about 52% of the sales happen between September and December. November is the biggest month, February the smallest.
3. **Geography:** California, New York, Texas and Washington make up about 47% of all sales.
4. **Discounts destroy profit:** no order line without a discount lost money, but 96.8% of the lines with a discount of 30% or more lost money. Together they lose about $135k, nearly half of the total profit ($286k).
5. **Top product:** the Canon imageCLASS 2200 Advanced Copier ($61.6k), more than twice the second one.
6. **Matplotlib vs Seaborn:** Seaborn is faster and clearer for statistical charts; Matplotlib is better for custom details and extra lines on top. Both are static, so for hover and zoom (the map) Plotly is a better choice.

## Key insights – Mini-Project
1. **Top states by sales:** California ($457.7k), New York ($310.9k), Texas ($170.2k), Washington ($138.6k), Pennsylvania ($116.5k).
2. **New York vs California:** California sells ~47% more, but profit is almost the same ($76.4k vs $74.0k). New York's margin is 23.8% vs 16.7% in California.
3. **Outstanding customer in New York:** Tom Ashbrook (about $4.6k profit).
4. **Profitability by state:** 10 of 49 states lose money (Texas, Ohio, Pennsylvania, Illinois are the worst). Losing states give an average discount of about 32%, other states only about 2%.
5. **Pareto (profit):** yes. The top 20% of customers bring about 81.7% of the profit.
6. **Pareto (sales):** no. The top 20% of customers bring only about 48.1% of the sales.
7. **Cities:** New York City is first for both sales and profit. 7 of the top 20 cities by sales lose money (for example Philadelphia, Houston, Chicago).
8. **Marketing decision:** prioritize California, New York, Washington and Michigan (and small high-margin cities like Lafayette, Atlanta, Minneapolis, Newark). Review the discount policy in Texas, Ohio, Pennsylvania and Illinois before spending more marketing money there.
