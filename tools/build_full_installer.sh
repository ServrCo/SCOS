sh image.sh
cd ..
mkdir -p imgbins
cp -r installer/bins/. imgbins
cp SCOS.7z imgbins
7z a "SCOS_offline_installer.7z" ./imgbins/.