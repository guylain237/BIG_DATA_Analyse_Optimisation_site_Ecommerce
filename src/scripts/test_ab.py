from src.data.ab_testing import ab_test

def main():
    start_test = ab_test()
    start_test.repartition()
    
main()