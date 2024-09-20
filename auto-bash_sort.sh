#!/bin/bash

#!/bin/bash

Ename="bash_files"

# Check if the directory already exists
if [ -d "$Ename" ]; then
  echo "Directory $Ename already exists."
else
  mkdir "$Ename"
  echo "Directory $Ename created."
fi

# Copy all .sh files to the directory
for fil in *.sh; do
  cp "$fil" "$Ename"
done

echo "All .sh files copied to $Ename."
