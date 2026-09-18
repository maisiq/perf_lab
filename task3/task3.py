import json
import sys


def main():
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    values = {}
    with open(values_path, mode="r", encoding="utf8") as f:
        data = json.load(f)
        for d in data["values"]:
            values[d["id"]] = d["value"]

    with open(tests_path, mode="r", encoding="utf8") as f:
        tests = json.load(f)

    report = tests

    def fn(test):
        test_id = test["id"]

        value = values.get(test_id)
        if value is None:
            print("No value for test_id: ", test_id)
        else:
            test["value"] = value

        inner_tests = test.get("values", [])
        for test in inner_tests:
            fn(test)

    with open(report_path, mode="w", encoding="utf8") as f:
        for test in tests.get("tests"):
            fn(test)

        json.dump(report, f, ensure_ascii=False, indent=3)


if __name__ == "__main__":
    main()
