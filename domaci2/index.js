// ----- SLIDER (Volume) -----
const slider = document.getElementById("myRange");
const volumeValue = document.getElementById("volume-value");

// Ažuriranje prikaza jačine zvuka
slider.oninput = function () {
  volumeValue.innerText = this.value;
};

// ----- BANKS (dva seta zvukova) -----
const bankOne = [
  { keyCode: 81, keyTrigger: "Q", id: "Heater-1", url: "https://s3.amazonaws.com/freecodecamp/drums/Heater-1.mp3" },
  { keyCode: 87, keyTrigger: "W", id: "Heater-2", url: "https://s3.amazonaws.com/freecodecamp/drums/Heater-2.mp3" },
  { keyCode: 69, keyTrigger: "E", id: "Heater-3", url: "https://s3.amazonaws.com/freecodecamp/drums/Heater-3.mp3" },
  { keyCode: 65, keyTrigger: "A", id: "Heater-4", url: "https://s3.amazonaws.com/freecodecamp/drums/Heater-4_1.mp3" },
  { keyCode: 83, keyTrigger: "S", id: "Clap", url: "https://s3.amazonaws.com/freecodecamp/drums/Heater-6.mp3" },
  { keyCode: 68, keyTrigger: "D", id: "Open-HH", url: "https://s3.amazonaws.com/freecodecamp/drums/Dsc_Oh.mp3" },
  { keyCode: 90, keyTrigger: "Z", id: "Kick-n'-Hat", url: "https://s3.amazonaws.com/freecodecamp/drums/Kick_n_Hat.mp3" },
  { keyCode: 88, keyTrigger: "X", id: "Kick", url: "https://s3.amazonaws.com/freecodecamp/drums/RP4_KICK_1.mp3" },
  { keyCode: 67, keyTrigger: "C", id: "Closed-HH", url: "https://s3.amazonaws.com/freecodecamp/drums/Cev_H2.mp3" }
];

const bankTwo = [
  { keyCode: 81, keyTrigger: "Q", id: "Chord-1", url: "https://s3.amazonaws.com/freecodecamp/drums/Chord_1.mp3" },
  { keyCode: 87, keyTrigger: "W", id: "Chord-2", url: "https://s3.amazonaws.com/freecodecamp/drums/Chord_2.mp3" },
  { keyCode: 69, keyTrigger: "E", id: "Chord-3", url: "https://s3.amazonaws.com/freecodecamp/drums/Chord_3.mp3" },
  { keyCode: 65, keyTrigger: "A", id: "Shaker", url: "https://s3.amazonaws.com/freecodecamp/drums/Give_us_a_light.mp3" },
  { keyCode: 83, keyTrigger: "S", id: "Open-HH", url: "https://s3.amazonaws.com/freecodecamp/drums/Dry_Ohh.mp3" },
  { keyCode: 68, keyTrigger: "D", id: "Closed-HH", url: "https://s3.amazonaws.com/freecodecamp/drums/Bld_H1.mp3" },
  { keyCode: 90, keyTrigger: "Z", id: "Punchy-Kick", url: "https://s3.amazonaws.com/freecodecamp/drums/punchy_kick_1.mp3" },
  { keyCode: 88, keyTrigger: "X", id: "Side-Stick", url: "https://s3.amazonaws.com/freecodecamp/drums/side_stick_1.mp3" },
  { keyCode: 67, keyTrigger: "C", id: "Snare", url: "https://s3.amazonaws.com/freecodecamp/drums/Brk_Snr.mp3" }
];

let currentBank = bankOne;

// ----- POWER -----
let powerOn = false; // startuje ugašeno
const soundNameElement = document.getElementById("sound-name");
const powerSwitch = document.getElementById("power-switch");

powerSwitch.addEventListener("change", function () {
  powerOn = this.checked;
  soundNameElement.innerText = powerOn ? "Power: ON" : "Power: OFF";
  soundNameElement.style.color = powerOn ? "green" : "red";
});

// ----- BANK SWITCH -----
const bankSwitch = document.getElementById("bank-switch");

bankSwitch.addEventListener("change", function () {
  currentBank = this.checked ? bankTwo : bankOne;
  soundNameElement.innerText = this.checked ? "Bank: 2" : "Bank: 1";
});

// ----- PLAY SOUND -----
const buttons = document.querySelectorAll(".button");

// Klik mišem
buttons.forEach((button) => {
  button.addEventListener("click", (e) => {
    playSound(e.target.innerHTML);
  });
});

// Pritiskanje tipki na tastaturi
document.addEventListener("keydown", (e) => {
  playSound(e.key.toUpperCase());
});

function playSound(keyTrigger) {
  if (!powerOn) return; // ako je ugašeno - ne svira

  const sound = currentBank.find((s) => s.keyTrigger === keyTrigger);
  if (!sound) return; // ako ne postoji taster

  const audio = new Audio(sound.url);
  audio.volume = slider.value / 100; // glasnoća
  audio.play();

  soundNameElement.innerText = sound.id; // ispiši ime zvuka
}
