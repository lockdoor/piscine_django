import antigravity
import sys

def myfunc():
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), b'{sys.argv[3]}')
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    myfunc()