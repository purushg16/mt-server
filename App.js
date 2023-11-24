//Import express.js module and create its variable.
const express=require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');
const multer = require('multer');
const uuid= require('uuid');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({extended:true}));

const PORT = process.env.PORT || 8000;

const storage =
    multer.diskStorage({
    destination: path.join(__dirname, 'pdfs'), // destination folder
    filename: (req, file, cb) => {
        cb(null, uuid.v4() + path.extname(file.originalname));
    }
});

console.log(__dirname);
const pythonPath = '/bin/python3'
// const pythonPath = path.join(__dirname, '/usr/bin/python3')

const upload =
    multer({
        storage,
        // dest: path.join(__dirname, 'pdfs/'), // destination folder
        limits: {fileSize: 3500000}, // size we will acept, not bigger
        fileFilter: (req, file, cb) => {
            const filetypes = /pdf/; // filetypes you will accept
            const mimetype = filetypes.test(file.mimetype); // verify file is == filetypes you will accept
            const extname = filetypes.test(path.extname(file.originalname)); // extract the file extension
            // if mimetype && extname are true, then no error
            if(mimetype && extname){
                return cb(null, true);
            }
            // if mimetype or extname false, give an error of compatibilty
            return cb("The uploaded file, isn't compatible :( we're sorry");
        }})

const pythonScript = './script.py';

//Import PythonShell module.
const {PythonShell} = require('python-shell');

app.post('/upload', upload.single('pdfFile'), (req, res) => {
    console.log('Called!');
    console.log('File Uploading started...');
    
    const filePath = req.file.path;
    const fileName = req.file.filename;
    const password = req.body.password;
    const threshold = Number(req.body.threshold) > 0 ? req.body.threshold : 0;
    
    console.log( threshold );
    const args = [ filePath, password, fileName, threshold ]
	// Here are the option object in which arguments can be passed for the python_test.js.

	let options = {
		mode: 'text',
        pythonPath: pythonPath,
		pythonOptions: ['-u'], // get print results in real-time
		args: args //An argument which can be accessed in the script using sys.argv[1]
	};
	
	// Create a PythonShell instance
    const pythonShell = new PythonShell(pythonScript, options);

    // Handle the output from the Python script
    pythonShell.on('message', (message) => { console.log(message); });

    // Handle errors (if any)
    pythonShell.on('error', (err) => { console.error('Python script error:', err) });

    // End the PythonShell instance
    pythonShell.end((err) => {
        if (err){ 
            res.status(400).send('Some error! Try again Later!');
            console.error('Python shell process ended with error:', err); 
        }
        else{ 
            res.send('Success');
            console.log('Python shell process finished.'); 
        }
        
        try {
            fs.unlinkSync( "decrypted_ "+ fileName +".pdf" );
            console.log('File deleted successfully.');
        } catch (err){ console.log('Error deleting the decryted file'); }

        try {
            fs.unlinkSync( "./pdfs/"+ fileName );
            console.log('File deleted successfully.');
        } catch (err){ 'File Not Found!' }
    });

});

app.listen(PORT, ()=>console.log(`Server connected to ${PORT}`));
