import 'package:flutter/material.dart';
import 'tattoo_simulator.dart';

void main() {
  runApp(const TattooSimulatorApp());
}

class TattooSimulatorApp extends StatelessWidget {
  const TattooSimulatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tattoo Simulator',
      theme: ThemeData.dark(),
      home: TattooSimulator(),
    );
  }
}