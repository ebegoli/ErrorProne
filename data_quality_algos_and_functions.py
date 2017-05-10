# --------------------------------------------------------------------------
# print_data_quality_report - Prints a data quality report that includes:
#                               - Available columns
#                               - For each column:
#                               - Data type
#                               - Count of missing values
#                               - Count of present values
#                               - Number of unique values
#                               - Minimum value
#                               - Maximum value
#
# Parameters - pandas dataFrame
#
# --------------------------------------------------------------------------

def print_data_quality_report(data):
    columns = pd.DataFrame(list(data.columns.values))
    data_types = pd.DataFrame(data.dtypes, columns=['Data Type'])
    missing_data_counts = pd.DataFrame(data.isnull().sum(), columns = ['Missing Values'])
    present_data_counts = pd.DataFrame(data.count(), columns=['Present Values'])
    
    # Loops through data columns and collects number of unique values 
    unique_value_counts = pd.DataFrame(columns=['Unique Values'])
    for v in list(data.columns.values):
        unique_value_counts.loc[v] = [data[v].nunique()]
        
    # Loops through data columns and collects minimum values
    minimum_values = pd.DataFrame(columns=['Minimum Value'])
    for v in list(data.columns.values):
        minimum_values.loc[v] = [data[v].min()]
        
    # Loops through data columns and collects maximum values
    maximum_values = pd.DataFrame(columns=['Maximum Value'])
    for v in list(data.columns.values):
        maximum_values.loc[v] = [data[v].max()]
    
    # Join all dataFrames
    data_quality_report = data_types.join(present_data_counts).join(missing_data_counts).join(unique_value_counts).join(minimum_values).join(maximum_values)

    print("\nData Quality Report")
    print("Total records: {}".format(len(data.index)))
    print(data_quality_report)
