#!/usr/bin/venv zsh

# Use this to set the new config value, needs 2 parameters.
# You could check that $1 and $2 is set, but I am lazy
function set_config(){
	# sed -i 's/find/replace/' file
	sed -i "/${TARGET}/${REPLACEMENT}" ${FILENAME}

}


# INITIALIZE CONFIG IF IT'S MISSING
if [ ! -e "${CONFIG}" ] ; then
    # Set default variable value
    sudo touch $CONFIG
    echo "myname=\"Test\"" | sudo tee --append $CONFIG
fi


for FILENAME in $CONFIG_LIST; do
	sed -i "/${TARGET}/${REPLACEMENT}" ${FILENAME}

	CONFIG="/tmp/test.cfg"

# LOAD THE CONFIG FILE
source $CONFIG

echo "${myname}" # SHOULD OUTPUT DEFAULT (test) ON FIRST RUN
myname="Erl"
echo "${myname}" # SHOULD OUTPUT Erl
set_config myname $myname # SETS THE NEW VALUE
