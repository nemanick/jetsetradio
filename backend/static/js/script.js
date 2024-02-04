function toggleDropdown() {
    var dropdownContent = document.getElementById("myDropdown");
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
    } else {
        dropdownContent.style.display = "flex";
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown-link') && !event.target.matches('.dropdown-content a')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "flex") {
                openDropdown.style.display = "none";
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var audioPlayer = document.getElementById('audioPlayer');
    var playPauseBtn = document.getElementById('playPauseBtn');
    var playBtn = document.querySelector('.play-icon');
    var pauseBtn = document.querySelector('.pause-icon');
    var seekBar = document.getElementById('seekBar');
    var currentTime = document.getElementById('currentTime');
    var duration = document.getElementById('duration');
    var repeatBtn = document.getElementById('repeatBtn');

    playPauseBtn.addEventListener('click', function () {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playPauseBtn.classList.add('playing');
            playBtn.classList.add('hidden-playPauseBtn');
            pauseBtn.classList.remove('hidden-playPauseBtn');
        } else {
            audioPlayer.pause();
            playPauseBtn.classList.remove('playing');
            playBtn.classList.remove('hidden-playPauseBtn');
            pauseBtn.classList.add('hidden-playPauseBtn');
        }
    });

    repeatBtn.addEventListener('click', function () {
        audioPlayer.loop = !audioPlayer.loop;
        repeatBtn.classList.toggle('active', audioPlayer.loop);
    });

    audioPlayer.addEventListener('timeupdate', function () {
        var minutes = Math.floor(audioPlayer.currentTime / 60);
        var seconds = Math.floor(audioPlayer.currentTime % 60);
        currentTime.textContent = minutes + ':' + (seconds < 10 ? '0' : '') + seconds;

        var durationMinutes = Math.floor(audioPlayer.duration / 60);
        var durationSeconds = Math.floor(audioPlayer.duration % 60);
        duration.textContent = durationMinutes + ':' + (durationSeconds < 10 ? '0' : '') + durationSeconds;

        seekBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    });

    seekBar.addEventListener('input', function () {
        var seekTime = (seekBar.value / 100) * audioPlayer.duration;
        audioPlayer.currentTime = seekTime;
    });
    
});

function toggleRepeat() {
    var repeatBtn = document.getElementById('repeatBtn');
    
    var currentColor = repeatBtn.querySelector('svg').getAttribute('fill');
    var newColor = (currentColor === '#ffffff') ? '#0026ff' : '#ffffff';

    repeatBtn.querySelector('svg').setAttribute('fill', newColor);
}
