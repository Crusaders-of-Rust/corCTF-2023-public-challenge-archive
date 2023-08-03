mkdir source
cp -r freecloud/* source
rm source/flag.txt source/db.sqlite3
cp fake_flag.txt source/flag.txt
tar -czvf source.tar.gz source
rm -rf source
mv source.tar.gz freecloud/media/uploads/
