
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Jeffh1505/Robotic-Arm">
    <img src="Images/Blue and White Simple Icon Engineering Logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">MechArm Robotic Arm</h3>

  <p align="center">
    An innovative robotic arm project featuring a Raspberry Pi Pico, SG90 servos, and a PCA9685 board for precise control.
    <br />
    <a href="https://github.com/Jeffh1505/Robotic-Arm"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Jeffh1505/Robotic-Arm">View Demo</a>
    ·
    <a href="https://github.com/Jeffh1505/Robotic-Arm/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Jeffh1505/Robotic-Arm/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#mechanical-components">Mechanical Components</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- Side-by-side images -->
<div align="center">
  <img src="https://github.com/Jeffh1505/Robotic-Arm/blob/ca8d28577ea20a32f708dfd36b841a662abd08b3/Images/Screenshot%202024-07-26%20163946.png" alt="CAD Screenshot" width="400" style="margin-right: 20px;"/>
  <img src="https://github.com/Jeffh1505/Robotic-Arm/blob/ca8d28577ea20a32f708dfd36b841a662abd08b3/Images/20240727_005540836_iOS.jpg" alt="Actual Robot" width="400"/>
</div>

The **Jeffrey Hernandez Robotic Arm** is an advanced robotic arm project designed for precision and versatility. It uses a Raspberry Pi Pico as the central control unit, integrated with SG90 servos for movement and a PCA9685 board for expanded servo control. The project aims to explore and demonstrate the capabilities of servo-based robotics with a user-friendly interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![MicroPython][MicroPython]][MicroPython-url]
* [![Raspberry Pi][Raspberry Pi]][RaspberryPi-url]
* [![PCA9685][PCA9685]][PCA9685-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Mechanical Components

The robotic arm's mechanical components are all 3D printed (in my case on a Bambu Labs A1 Mini).  You can find the design files for the parts in the repository. The files include both .STL and .STEP formats, allowing you to view and modify them using popular 3D modeling software.

* **[Links to STL Files](https://github.com/Jeffh1505/Robotic-Arm/tree/main/mechanical_components/stl](https://github.com/Jeffh1505/Robotic-Arm/tree/d86a44941792ed8565e8fd56f3d0de753aeca986/STL%20Files))**
* **[Links to STEP Files](https://github.com/Jeffh1505/Robotic-Arm/tree/main/mechanical_components/step](https://github.com/Jeffh1505/Robotic-Arm/tree/d86a44941792ed8565e8fd56f3d0de753aeca986/STEP%20Files))**

These files cover all the parts necessary to assemble the robotic arm, including the links, claw mechanism, and mounting brackets. Make sure to check the provided assembly instructions for guidance on how to put everything together.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [MicroPython](https://micropython.org/) - Python for microcontrollers
* [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) - Microcontroller
* [PCA9685 Board](https://www.adafruit.com/product/815) - PWM Driver for Servo Control
* [SG90 Servos](https://www.dfrobot.com/product-1118.html) - Servos for movement

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jeffh1505/Robotic-Arm.git
   ```
2. Navigate to the project directory
   ```sh
   cd Robotic-Arm
   ```
3. Install dependencies (if applicable)
   ```sh
   pip install -r requirements.txt
   ```
4. Flash the firmware to the Raspberry Pi Pico using the MicroPython firmware and upload the project code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To control the robotic arm, you can use the joystick module and the push button to manipulate the arm's movement and claw. Connect the components as described in the wiring diagram and run the provided MicroPython script to start controlling the robotic arm.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Implement advanced control algorithms
- [ ] Add user interface for easier operation
- [ ] Improve calibration and accuracy of servos
    - [ ] Refine servo response
    - [ ] Enhance feedback mechanisms

See the [open issues](https://github.com/Jeffh1505/Robotic-Arm/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jeffrey Hernandez  - jnh2147@columbia.edu

Project Link: [https://github.com/Jeffh1505/Robotic-Arm](https://github.com/Jeffh1505/Robotic-Arm)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Adafruit](https://www.adafruit.com) - For the PCA9685 board and servos
* [Raspberry Pi Foundation](https://www.raspberrypi.com) - For the Raspberry Pi Pico
* [MicroPython Community](https://micropython.org/community) - For the MicroPython firmware and support

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Jeffh1505/Robotic-Arm.svg?style=for-the-badge
[contributors-url]: https://github.com/Jeffh1505/Robotic-Arm/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Jeffh1505/Robotic-Arm.svg?style=for-the-badge
[forks-url]: https://github.com/Jeffh1505/Robotic-Arm/network/members
[stars-shield]: https://img.shields.io/github/stars/Jeffh1505/Robotic-Arm.svg?style=for-the-badge
[stars-url]: https://github.com/Jeffh1505/Robotic-Arm/stargazers
[issues-shield]: https://img.shields.io/github/issues/Jeffh1505/Robotic-Arm.svg?style=for-the-badge
[issues-url]: https://github.com/Jeffh1505/Robotic-Arm/issues
[license-shield]: https://img.shields.io/github/license-MIT-blue/Jeffh1505/Robotic-Arm.svg?style=for-the-badge
[license-url]: https://github.com/Jeffh1505/Robotic-Arm/blob/de5ad141a244e4c7955a105685d15317e0745402/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jeffreyhernandez
[product-screenshot]: https://github.com/Jeffh1505/Robotic-Arm/blob/2bc25584afa35375e4da769b79eef2e5bba5cad9/Images/Screenshot%202024-07-26%20163946.png
[MicroPython]: https://img.shields.io/badge/MicroPython-black?logo=micropython
[MicroPython-url]: https://micropython.org/
[Raspberry Pi]: https://img.shields.io/badge/Raspberry%20Pi-dark%20green?logo=raspberrypi
[RaspberryPi-url]: https://www.raspberrypi.com/
[PCA9685]: https://img.shields.io/badge/PCA9685-blue?logo=python
[PCA9685-url]: https://www.adafruit.com/product/815
```

Feel free to make any additional adjustments or customizations based on your project needs!
