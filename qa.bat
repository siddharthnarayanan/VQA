md dssm
md dssm\model

REM shuffle the training data
REM ..\bin\WordHash.exe --shuffle data\train.pair.tok.tsv data\train.sf.tsv

REM generate features
REM ..\bin\WordHash.exe --pair2seqfea data\train.pair.tok.tsv data\l3g.txt data\l3g.txt 1 dssm\train

REM convert feature files into binary files
..\bin\WordHash.exe --seqfea2bin  dssm\train.ques.src.fea.full 1024 dssm\train.ques.src.fea.full.bin
..\bin\WordHash.exe --seqfea2bin  dssm\train.ans.src.fea.full 1024 dssm\train.ans.src.fea.full.bin

REM compute "noise distribution" which is approximated by scaled unigram distribution for NCE training.
REM ..\bin\ComputelogPD.exe /i data\train.pair.tok.tsv /o mix\train.logpD.s75 /C 1 /S 0.75

REM cdssm training
..\bin\DSSM_Train.exe Q_A.config.txt

REM perform sent2vec using the trained model to dev set
REM ..\bin\sent2vec /inSrcModel dssm\model\dssm_QUERY_DONE /inSrcVocab data\l3g.txt /inSrcModelType DSSM /inTgtModel dssm\model\dssm_DOC_DONE /inTgtVocab data\l3g.txt /inTgtModelType DSSM /inFilename data\dev.pair.tok.tsv /outFilenamePrefix dssm\dev.sent2vec
