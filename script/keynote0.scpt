tell application "Keynote"
	set doc to open "/Users/peter/Dropbox/onderwijs/Machine Learning/2021/Lectures/11 Introduction/11.Introduction.0.key"
	export doc as slide images to "/Users/peter/Dropbox/gits/git-sakhmet/mlvu.github.io/script/test" with properties {image format:JPEG, compression factor:0.65}
	close saving yes
end tell