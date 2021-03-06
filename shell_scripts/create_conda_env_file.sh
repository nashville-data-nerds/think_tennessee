#!/bin/bash
# Create environment file
conda env export --no-builds > ../environment.yml

# Remove bad packages
sed -i ".bak" '/llvm-openmp/d' ../environment.yml
sed -i ".bak" '/libcxxabi/d' ../environment.yml
sed -i ".bak" '/appnope/d' ../environment.yml
sed -i ".bak" '/libgfortran/d' ../environment.yml
sed -i ".bak" '/libcxx/d' ../environment.yml

# Add datanerdpy to environment file
sed -i ".bak" 's~datanerdpy==1.0.0~--editable=git+git://github.com/nashville-data-nerds/datanerdpy#egg=datanerdpy~g' ../environment.yml

rm ../environment.yml.bak



