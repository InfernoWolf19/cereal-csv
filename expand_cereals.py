import csv

def main():
    retailers = ["Aldi", "Asda", "Lidl", "M&S", "Morrisons", "Sainsbury's", "Tesco", "Waitrose"]

    brand_mapping = {r: {} for r in retailers}

    with open('cereals.csv', 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in rows:
        if row['Retailer'] in brand_mapping:
            if row['Brand_Type'] not in brand_mapping[row['Retailer']]:
                brand_mapping[row['Retailer']][row['Brand_Type']] = row['Brand_Name']

    # Templates for new SKUs
    templates = [
        # Standard own-brand templates
        ("Standard Own-Brand", "Instant Porridge Pots Original", "Oats", 370, 10.5, 7.5, 1.2, 8.5, 1.5, 0.05, "100% Whole Oat", "Plain/Natural", "Unsweetened", "None", "Minimal (2-4)", "Processed (NOVA 3)", 0.50),
        ("Standard Own-Brand", "Instant Porridge Pots Golden Syrup", "Oats", 380, 9.5, 6.5, 1.0, 7.5, 15.0, 0.2, "100% Whole Oat", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Minimal (2-4)", "Processed (NOVA 3)", 0.60),
        ("Standard Own-Brand", "Instant Porridge Pots Apple & Blueberry", "Oats", 375, 9.0, 6.0, 1.0, 7.0, 18.0, 0.15, "100% Whole Oat", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Processed (NOVA 3)", 0.65),
        ("Standard Own-Brand", "Gluten Free Oats", "Oats", 374, 11.0, 8.0, 1.5, 9.0, 1.0, 0.01, "100% Whole Oat", "Plain/Natural", "Unsweetened", "None", "Single Ingredient (1)", "Processed Culinary/Milled (NOVA 2)", 0.30),
        ("Standard Own-Brand", "Gluten Free Corn Flakes", "Flakes & Puffs", 378, 7.0, 1.0, 0.2, 3.0, 8.0, 1.1, "Corn", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Minimal (2-4)", "Ultra-Processed/UPF (NOVA 4)", 0.35),
        ("Standard Own-Brand", "Gluten Free Crisp Rice", "Flakes & Puffs", 382, 6.5, 1.0, 0.2, 2.0, 8.0, 1.0, "Rice", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Minimal (2-4)", "Ultra-Processed/UPF (NOVA 4)", 0.40),
        ("Standard Own-Brand", "Organic Porridge Oats", "Oats", 374, 11.0, 8.0, 1.5, 9.0, 1.0, 0.01, "100% Whole Oat", "Plain/Natural", "Unsweetened", "None", "Single Ingredient (1)", "Processed Culinary/Milled (NOVA 2)", 0.25),
        ("Standard Own-Brand", "Organic Bran Flakes", "Bran & Fibre", 360, 14.0, 2.1, 0.4, 15.0, 14.0, 0.8, "100% Whole Wheat", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Processed (NOVA 3)", 0.30),
        ("Standard Own-Brand", "Toasted Flakes of Corn with Strawberry", "Flakes & Puffs", 380, 7.0, 1.5, 0.3, 3.5, 15.0, 0.9, "Corn", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.20),
        ("Standard Own-Brand", "Cinnamon Squares", "Kids & Sweet", 405, 6.0, 8.5, 1.5, 4.0, 25.0, 0.7, "100% Whole Wheat", "Cinnamon", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.25),
        ("Standard Own-Brand", "Fruit Rings", "Kids & Sweet", 385, 7.0, 3.0, 0.8, 4.0, 20.0, 0.6, "Multigrain", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.25),
        ("Standard Own-Brand", "Cookie Hoops", "Kids & Sweet", 390, 7.5, 4.0, 1.2, 4.5, 22.0, 0.7, "Multigrain", "Chocolate", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.28),
        ("Standard Own-Brand", "Honey Loops", "Kids & Sweet", 385, 7.5, 3.5, 0.7, 4.5, 24.0, 0.65, "Multigrain", "Honey/Nut", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.25),
        ("Standard Own-Brand", "Choco Flakes", "Kids & Sweet", 395, 6.5, 2.5, 1.0, 3.5, 25.0, 0.7, "Multigrain", "Chocolate", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.25),
        ("Standard Own-Brand", "Berry Granola", "Granola", 440, 9.5, 15.0, 3.0, 7.5, 16.0, 0.05, "100% Whole Oat", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.30),
        ("Standard Own-Brand", "Tropical Granola", "Granola", 445, 9.0, 14.5, 4.5, 7.0, 18.0, 0.05, "100% Whole Oat", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.32),
        ("Standard Own-Brand", "Nut Granola", "Granola", 460, 11.5, 21.0, 4.0, 8.0, 12.0, 0.05, "100% Whole Oat", "Honey/Nut", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.35),
        ("Standard Own-Brand", "Chocolate Granola", "Granola", 455, 9.5, 18.0, 5.0, 6.5, 20.0, 0.1, "100% Whole Oat", "Chocolate", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.33),
        ("Standard Own-Brand", "Orchard Fruits Muesli", "Muesli", 365, 10.0, 5.0, 0.8, 9.0, 18.0, 0.05, "Multigrain", "Fruit/Berry", "Naturally Sweetened (Dried Fruit)", "None", "Moderate (5-8)", "Processed (NOVA 3)", 0.25),
        ("Standard Own-Brand", "Red Berry Muesli", "Muesli", 360, 9.5, 4.5, 0.7, 9.5, 16.0, 0.05, "Multigrain", "Fruit/Berry", "Naturally Sweetened (Dried Fruit)", "None", "Moderate (5-8)", "Processed (NOVA 3)", 0.28),
        ("Standard Own-Brand", "Crispy Rice & Wheat Flakes", "Flakes & Puffs", 375, 14.5, 1.5, 0.3, 5.0, 14.5, 0.9, "Multigrain", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.22),
        ("Standard Own-Brand", "Red Berries Crisp Flakes", "Flakes & Puffs", 372, 13.5, 1.5, 0.3, 5.5, 17.5, 0.85, "Multigrain", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.28),
        ("Standard Own-Brand", "Oat Clusters with Milk Chocolate", "Granola", 445, 9.5, 16.5, 4.5, 6.5, 21.0, 0.1, "100% Whole Oat", "Chocolate", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.29),
        ("Standard Own-Brand", "Puffed Wheat", "Flakes & Puffs", 355, 14.0, 2.0, 0.4, 10.0, 1.0, 0.05, "100% Whole Wheat", "Plain/Natural", "Unsweetened", "None", "Single Ingredient (1)", "Processed Culinary/Milled (NOVA 2)", 0.15),

        # Premium own-brand templates
        ("Premium Own-Brand", "Maple & Pecan Granola", "Granola", 465, 10.5, 20.0, 3.5, 7.5, 16.0, 0.05, "100% Whole Oat", "Honey/Nut", "Added Sugar/Syrup", "Maple Syrup", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.65),
        ("Premium Own-Brand", "Cranberry & Almond Granola", "Granola", 450, 11.0, 18.0, 2.5, 7.5, 15.0, 0.05, "100% Whole Oat", "Fruit/Berry", "Added Sugar/Syrup", "Honey", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.60),
        ("Premium Own-Brand", "Belgian Chocolate Chunk Granola", "Granola", 470, 9.5, 21.0, 7.5, 6.0, 21.0, 0.1, "100% Whole Oat", "Chocolate", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.68),
        ("Premium Own-Brand", "Macadamia & Coconut Muesli", "Muesli", 395, 10.0, 12.0, 4.5, 8.5, 14.0, 0.05, "Multigrain", "Honey/Nut", "Naturally Sweetened (Dried Fruit)", "None", "Moderate (5-8)", "Processed (NOVA 3)", 0.58),
        ("Premium Own-Brand", "Cherry & Berry Muesli", "Muesli", 365, 9.5, 5.0, 0.8, 9.0, 20.0, 0.05, "Multigrain", "Fruit/Berry", "Naturally Sweetened (Dried Fruit)", "None", "Moderate (5-8)", "Processed (NOVA 3)", 0.55),
        ("Premium Own-Brand", "Ancient Grains Granola", "Granola", 435, 12.0, 15.0, 2.5, 8.5, 12.0, 0.05, "Multigrain", "Plain/Natural", "Added Sugar/Syrup", "Honey", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.70),
        ("Premium Own-Brand", "Protein Crunch Blueberry", "High-Protein", 445, 22.0, 14.0, 2.0, 8.0, 10.0, 0.15, "100% Whole Oat", "Fruit/Berry", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.75),
        ("Premium Own-Brand", "Protein Crunch Peanut Butter", "High-Protein", 455, 24.0, 16.0, 2.5, 7.5, 9.0, 0.2, "100% Whole Oat", "Honey/Nut", "Added Sugar/Syrup", "Sugar", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.75),
        ("Premium Own-Brand", "Toasted Coconut Flakes & Seeds", "Granola", 460, 12.0, 22.0, 8.0, 9.0, 10.0, 0.05, "Multigrain", "Plain/Natural", "Added Sugar/Syrup", "Honey", "Complex (9+)", "Ultra-Processed/UPF (NOVA 4)", 0.65),

        # Value own-brand templates
        ("Value Own-Brand", "Crisp Rice", "Flakes & Puffs", 380, 7.0, 1.0, 0.2, 2.0, 8.0, 1.0, "Rice", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.10),
        ("Value Own-Brand", "Muesli", "Muesli", 365, 10.0, 5.0, 1.0, 8.0, 15.0, 0.1, "Multigrain", "Plain/Natural", "Naturally Sweetened (Dried Fruit)", "None", "Minimal (2-4)", "Processed (NOVA 3)", 0.08),
        ("Value Own-Brand", "Bran Flakes", "Bran & Fibre", 355, 13.5, 2.0, 0.4, 14.0, 15.0, 0.8, "100% Whole Wheat", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Minimal (2-4)", "Processed (NOVA 3)", 0.09),
        ("Value Own-Brand", "Honey Nut Flakes", "Kids & Sweet", 388, 6.5, 3.5, 0.5, 3.5, 28.0, 0.9, "Corn", "Honey/Nut", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.15),
        ("Value Own-Brand", "Frosted Flakes", "Kids & Sweet", 382, 4.5, 0.5, 0.1, 2.0, 36.0, 0.8, "Corn", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.14),
        ("Value Own-Brand", "Choco Snaps", "Kids & Sweet", 385, 6.0, 2.0, 1.0, 3.0, 26.0, 0.7, "Rice", "Chocolate", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.14),
        ("Value Own-Brand", "Multigrain Hoops", "Kids & Sweet", 370, 7.5, 3.5, 0.8, 8.5, 19.0, 0.7, "Multigrain", "Plain/Natural", "Added Sugar/Syrup", "Sugar", "Moderate (5-8)", "Ultra-Processed/UPF (NOVA 4)", 0.14),
    ]

    new_rows = []

    for retailer in retailers:
        for t in templates:
            brand_type = t[0]
            if brand_type not in brand_mapping[retailer]:
                continue

            brand_name = brand_mapping[retailer][brand_type]
            product_name = f"{brand_name} {t[1]}"

            new_row = {
                'Retailer': retailer,
                'Brand_Type': brand_type,
                'Brand_Name': brand_name,
                'Product_Name': product_name,
                'Sub_Category': t[2],
                'Kcal_per_100g': t[3],
                'Protein_g_per_100g': t[4],
                'Fat_g_per_100g': t[5],
                'Saturated_Fat_g_per_100g': t[6],
                'Fibre_g_per_100g': t[7],
                'Sugar_g_per_100g': t[8],
                'Salt_g_per_100g': t[9],
                'Base_Grain': t[10],
                'Flavour_Profile': t[11],
                'Sweetness_Profile': t[12],
                'Sweetener_Agent': t[13],
                'Ingredient_Count_Tier': t[14],
                'Processing_Tier': t[15],
                'Approx_Cost_per_100g_GBP': t[16]
            }
            new_rows.append(new_row)

    def sort_key(row):
        r = row['Retailer']
        if r == 'Multi-Retailer Brand':
            return (1, r, row['Brand_Type'], row['Brand_Name'], row['Product_Name'])
        else:
            bt_order = {'Value Own-Brand': 1, 'Standard Own-Brand': 2, 'Premium Own-Brand': 3}
            bt = bt_order.get(row['Brand_Type'], 4)
            return (0, r, bt, row['Brand_Name'], row['Product_Name'])

    all_rows = rows + new_rows
    all_rows.sort(key=sort_key)

    with open('cereals.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

if __name__ == '__main__':
    main()
