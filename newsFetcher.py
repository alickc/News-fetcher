import argparse
import constants, node

parser = argparse.ArgumentParser(description="Fetch News data to txt files from various websites")
parser.add_argument('-l','--links', nargs='+', metavar='',required=True, help='List of websites: ')
parser.add_argument('-k','--keywords', nargs='+', metavar='',required=True, help='List of keywords to be searched: ')
parser.add_argument('-p','--path', type=str, metavar='',required=True,help='path to save files')
parser.add_argument('-d','--driverpath',type=str, metavar='',required=True,help="Driver path for selenium")
parser.add_argument('-da','--dateafter',type=str, metavar='',required=True, help="Start date to google search(YYYY-MM-DD")

args = parser.parse_args()

if __name__ == '__main__':
    print("Fetching data with given params:\n Links:" + str(args.links) + "\n Keywords:" + str(args.keywords)
          + "\n Path:"+args.path + "\n DriverPath(selenium):"+args.driverpath + "\n DateAfter:"+args.dateafter+"\n")
    constants.path = args.path
    constants.driverPath = args.driverpath
    constants.date_after = args.dateafter
    node.start(args.links, args.keywords)