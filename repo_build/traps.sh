# trap_zerr() {
# 	echo "$0: Error Trapped: $?" >2
# }
# trap trap_zerr ZERR
# trap_err() {
# 	'echo "$0: Error Trapped: $?" >2'
# }
# trap trap_err ERR
# trap_exit() { 'echo "$0: Exit with code: $?"'; }

trap 'echo "LINE NUMBER: $LINENO"' DEBUG
trap 'echo "$0: Error Trapped: $?" >2' ERR
trap 'echo "$0: Exit with code: $?"' EXIT
