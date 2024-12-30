import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:http/http.dart' as http;

class TattooSimulator extends StatefulWidget {
  const TattooSimulator({super.key});

  @override
  _TattooSimulatorState createState() => _TattooSimulatorState();
}

class _TattooSimulatorState extends State<TattooSimulator> {
  String? uploadedFile;
  double xPos = 0, yPos = 0, scale = 100;
  String? renderImageUrl;

  Future<void> uploadFile() async {
    var picked = await FilePicker.platform.pickFiles(type: FileType.image);
    if (picked != null && picked.files.isNotEmpty) {
      setState(() {
        uploadedFile = picked.files.first.path;
      });

      // Send file to backend
      var request = http.MultipartRequest('POST', Uri.parse('http://<YOUR_SERVER_IP>:5000/upload'));
      request.files.add(await http.MultipartFile.fromPath('file', uploadedFile!));
      var response = await request.send();

      if (response.statusCode == 200) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('File uploaded successfully')));
      } else {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('File upload failed')));
      }
    }
  }

  Future<void> simulateTattoo() async {
    var response = await http.post(Uri.parse('http://<YOUR_SERVER_IP>:5000/simulate_tattoo'), body: {
      'x_pos': xPos.toString(),
      'y_pos': yPos.toString(),
      'scale': scale.toString(),
    });

    if (response.statusCode == 200) {
      setState(() {
        renderImageUrl = 'http://<YOUR_SERVER_IP>:5000/renders/output.png';
      });
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Tattoo simulated successfully')));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Tattoo simulation failed')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tattoo Simulator')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: uploadFile,
              child: const Text('Upload Tattoo'),
            ),
            if (uploadedFile != null) Text('Uploaded: $uploadedFile'),
            Slider(
              value: xPos,
              min: -200,
              max: 200,
              label: 'X Position: $xPos',
              onChanged: (value) => setState(() => xPos = value),
            ),
            Slider(
              value: yPos,
              min: -200,
              max: 200,
              label: 'Y Position: $yPos',
              onChanged: (value) => setState(() => yPos = value),
            ),
            Slider(
              value: scale,
              min: 25,
              max: 400,
              label: 'Scale: $scale%',
              onChanged: (value) => setState(() => scale = value),
            ),
            ElevatedButton(
              onPressed: simulateTattoo,
              child: const Text('Simulate Tattoo'),
            ),
            if (renderImageUrl != null)
              Expanded(
                child: Image.network(renderImageUrl!),
              ),
          ],
        ),
      ),
    );
  }
}