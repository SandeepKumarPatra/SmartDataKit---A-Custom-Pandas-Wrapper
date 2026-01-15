from src.wrangler import FinancialWrangler


def main():
    print("Starting SmartDataKit demo...\n")

    wrangler = FinancialWrangler("data/sample_sales.csv")

    # Chain cleaning operations
    wrangler \
        .clean_currency(["revenue", "expenses"]) \
        .remove_outliers("revenue")

    # Generate monthly report
    monthly_report = wrangler.get_monthly_report(
        date_col="transaction_date",
        value_col="revenue"
    )

    print("📊 Monthly Revenue Report")
    print(monthly_report)

    # Save cleaned data
    wrangler.save_clean_data("data/processed_sales.csv")


if __name__ == "__main__":
    main()
