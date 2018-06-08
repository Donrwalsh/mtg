from writer_service import Writer


class Helper:

    @classmethod
    def select(cls, list_of_things, key):
        for dict in list_of_things:
            if key in dict.keys():
                return str(dict[key])
        return 'null'

    @classmethod
    def select_for_query(cls, list_of_things, key):
        result = Helper.select(list_of_things, key)
        if result != 'null':
            result = "'" + result.replace("'", "''") + "'"
        return result


    @classmethod
    def validate_set(cls, subject, legend):
        for key in subject:
            if key == "type":
                check_key = "set_type"
            elif key == "release_date":
                check_key = "released_at"
            else:
                check_key = key
            if key != "id":
                if str(subject[key]) != str(Helper.select(legend, check_key)):
                    if str(subject[key]) == 'None' and str(Helper.select(legend, check_key) is 'null'):
                        pass
                    else:
                        Writer.error("data mismatch on " + subject['code'] + "[" + key + "]",
                            "   data-source: " + str(subject[key]) + ", database: " + str(Helper.select(legend, check_key)) + "\n")
                        return False
        return True
