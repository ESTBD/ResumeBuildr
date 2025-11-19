<script setup>
import { useResumeStore } from '~/stores/formStore'
const store = useResumeStore()

// const cv = document.querySelector('.resume');

// function scaleCV() {
//     const scale = Math.min(
//         window.innerWidth / cv.offsetWidth,
//         window.innerHeight / cv.offsetHeight,
//         1
//     );
//     cv.style.transform = `scale(${scale})`;
// }

// window.addEventListener('resize', scaleCV);
// window.addEventListener('load', scaleCV);
</script>

<template>

    <div id="resume-preview" class="resume">
        <div v-if="store.firstName.length || store.lastName.length">
            <h1 class="name">{{ store.firstName }} {{ store.lastName }}</h1>
        </div>

        <div v-if="store.jobTitle.length">
            <h2 class="jobTitle">{{ store.jobTitle }}</h2>
        </div>

        <div class="primary-info">
            <div v-if="store.address.length">
                <a :href="'https://maps.google.com/?q=' + store.address" target="_blank"><strong>Address:</strong> {{ store.address }}</a>
            </div>

            <div v-if="store.phone.length">
                <a :href="'tel:' + store.phone" target="_blank"><strong>Phone:</strong> {{ store.phone }}</a>
            </div>

            <div v-if="store.email.length">
                <a :href="'mailto:' + store.email" target="_blank"><strong>Email:</strong> {{ store.email }}</a>
            </div>
        </div>

        <div class="contact">
            <div v-for="(contact, index) in store.contacts" :key="index">
                <a :href="contact.link" target="_blank"><strong>{{ contact.platform }}</strong>: {{ contact.username }}</a>
            </div>
        </div>

        <div v-if="store.educations.length" class="educations">
            <div>
                <h3>Education</h3>

                <hr>
            </div>

            <div v-for="(edu, index) in store.educations" :key="index" class="education">
                <div class="hor-grp">
                    <div v-if="edu.inst.length">
                        <h4>{{ edu.inst }}</h4>
                    </div>

                    <div v-if="edu.location.length">
                        <p>{{ edu.location }}</p>
                    </div>
                </div>

                <div class="hor-grp">
                    <div v-if="edu.degree.length">
                        <p>{{ edu.degree }} {{ edu.sub !== undefined ? 'in ' + edu.sub : '' }}</p>
                    </div>
                    <div v-if="edu.sYearMonth.length || edu.eYearMonth.length">
                        <p>{{ edu.sYearMonth }} — {{ edu.eYearMonth }}</p>
                    </div>
                </div>

                <div v-if="edu.score > 0">
                    <p>{{ edu.resultType }}: {{ parseFloat(edu.score).toFixed(2) }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
* {
    font-family: monospace;
    font-size: 11px;
    flex-wrap: wrap;
}

.resume {
    width: 210mm;
    min-height: 297mm;
    margin: auto;
    padding: 35px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    transform-origin: top left;
    display: flex;
    flex-direction: column;
    gap: 8px;

}

@media print {
    .resume {
        transform: none !important;
        box-shadow: none;
    }
}

hr {
    border-color: black;
}

h1 {
    text-align: center;
    font-size: 24px;
}

h2 {
    text-align: center;
    font-size: 20px;
    font-weight: normal;
}

h3 {
    font-size: 18px;
}

h4 {
    font-size: 14px;
}

.primary-info,
.contact {
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    column-gap: 20px;
}

.educations {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 8px;
}

.hor-grp {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
</style>