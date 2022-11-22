[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## CSVto3Dstrings

CSVto3Dstrings is a useful tool to convert any CSV file into a 3-d array of strings in C. I created it after amassing a fairly large spreadsheet of musical scale and note values and wanted to convert those for use in a C program. This tool could be useful for anyone needing to keep track of various attributes within such a 3d array.

![product-screenshot]

### Built With

* [![Python][Python.org]][Python-url]
* [![Clang][Clang]][Clang-url]

### Installation

1. Download this repo to your local drive.
2. Open a terminal.
3. Navigate in your terminal to the folder containing this repo.

## Usage

1. Move your CSV files to the same folder as `csvto3dstrings.py`.
2. In the terminal, execute with the following usage: `python csvto3dstrings.py INPUTFILE OUTPUTFILE STRUCTURENAME`. For example, you might execute `python csvto3dstrings.py scales.csv scales.h myScales`. Notice that `scales.csv` in the inputfile, `scales.h` is the output file, and the name of the 3-d array is `myScales`.
3. For testing purposes, the above referenced input file is included in the repo for testing.

## Contributing

Your contributions to this project are very much appreciated. If you would like to help make this project better, fork to repo and create a pull request. Alternatively, you can open an issue with the tag "request." Please star this project!

1. Fork the Project and make a branch with your feature (`git checkout -b feature/myFeature`).
3. Commit your Changes (`git commit -m 'Added myFeature'`).
4. Push to the Branch (`git push origin feature/myFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Pending...

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/guyewhite/CSVto3Dstrings.svg?style=for-the-badge
[contributors-url]: https://github.com/guyewhite/CSVto3Dstrings/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/guyewhite/CSVto3Dstrings.svg?style=for-the-badge
[forks-url]: https://github.com/guyewhite/CSVto3Dstrings/network/members
[stars-shield]: https://img.shields.io/github/stars/guyewhite/CSVto3Dstrings.svg?style=for-the-badge
[stars-url]: https://github.com/guyewhite/CSVto3Dstrings/stargazers
[issues-shield]: https://img.shields.io/github/issues/guyewhite/CSVto3Dstrings.svg?style=for-the-badge
[issues-url]: https://github.com/guyewhite/CSVto3Dstrings/issues
[license-shield]: https://img.shields.io/github/license/guyewhite/CSVto3Dstrings.svg?style=for-the-badge
[license-url]: https://github.com/guyewhite/CSVto3Dstrings/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python.org]: https://img.shields.io/badge/python-version?style=for-the-badge&logo=python&logoColor=FFFFFF
[Python-url]: https://python.org
[Clang]: https://img.shields.io/badge/Clang-version?style=for-the-badge&logo=C&logoColor=FFFFFF
[Clang-url]: https://clang.llvm.org/
