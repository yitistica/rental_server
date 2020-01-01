import pymysql


class MySqlOperations(object):
    def __init__(self):
        self.mysql_client = None

    def inject_client(self, mysql_client):
        self.mysql_client = mysql_client

    def delete_table(self, table_name):
        sql = f"DROP TABLE IF EXISTS {table_name}; "
        cursor = self.mysql_client.cursor()
        cursor.execute(sql)
        self.mysql_client.commit()

    def truncate_table(self, table_name):
        sql = f"truncate {table_name};"
        cursor = self.mysql_client.cursor()
        cursor.execute(sql)
        self.mysql_client.commit()

    def retrieve_data(self, sql, return_dict=False):
        if return_dict:
            cursor = self.mysql_client.cursor(pymysql.cursors.DictCursor)
        else:
            cursor = self.mysql_client.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def execute_sql(self, sql):
        cursor = self.mysql_client.cursor()
        cursor.execute(sql)
        self.mysql_client.commit()

    def execute_sql_block(self, sql_lines):
        cursor = self.mysql_client.cursor()
        for line in sql_lines:
            cursor.execute(line)
        self.mysql_client.commit()

    def execute_bulk_insertion(self, table_name, variables: list, data: list, batch_size=10000):
        variables_str = '(' + ','.join(variables) + ')'
        variable_place_holder = '(' + ','.join(['%s'] * len(variables)) + ')'

        data_batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
        for which_batch, data_batch in enumerate(data_batches):
            converted_data = []
            for data_dict in data_batch:
                data_list = []
                for variable in variables:
                    data_list.append(data_dict[variable])
                converted_data.append(tuple(data_list))

            sql = f"INSERT INTO {table_name} {variables_str} VALUES {variable_place_holder}"
            cursor = self.mysql_client.cursor()
            cursor.executemany(sql, converted_data)
            self.mysql_client.commit()

    def execute_bulk_update(self, table_name, variables: list, data: list, batch_size=10000):
        variables_str = '(' + ','.join(variables) + ')'
        variable_place_holder = '(' + ','.join(['%s'] * len(variables)) + ')'

        data_batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
        for which_batch, data_batch in enumerate(data_batches):
            print(f"updating {which_batch} / {len(data_batches)}.")
            converted_data = []
            for data_dict in data_batch:
                data_list = []
                for variable in variables:
                    value = data_dict[variable]
                    data_list.append(value)
                converted_data.append(tuple(data_list))

            sql = f"REPLACE INTO {table_name} {variables_str} VALUES {variable_place_holder}"
            cursor = self.mysql_client.cursor()
            cursor.executemany(sql, converted_data)
            # try:
            #     cursor.executemany(sql, converted_data)
            # except:
            #     raise Exception(sql)
            self.mysql_client.commit()

    def check_if_row_exist(self, table_name, row: dict):
        pass




