<script setup>
import { useResumeStore } from '~/stores/formStore'
import { onMounted } from 'vue'

const store = useResumeStore()

onMounted(() => {
    store.loadFromLocalStorage()

    store.$subscribe((mutation, state) => {
        localStorage.setItem('resumeData', JSON.stringify(state))
    })
})

const submitForm = async () => {
    const resumeData = {
        firstname: store.firstName,
        lastname: store.lastName,
        email: store.email,
        address: store.address,
        jobtitle: store.jobTitle,
        contacts: store.contacts.map(contact => ({
            platform_name: contact.platform,
            profile_link: contact.link
        })),
        educations: store.educations.map(edu => ({
            school_name: edu.school,
            degree: edu.degree,
            start_time: edu.sYearMonth,
            end_time: edu.eYearMonth,
            result_type: edu.resultType,
            score: edu.score
        })),
        experiences: store.experiences.map(exp => ({
            company: exp.company,
            role: exp.role,
            start_time: exp.sYearMonth,
            end_time: exp.eYearMonth,
            description: exp.desc
        })),
        projects: store.projects.map(pro => ({
            project_name: pro.name,
            project_link: pro.link,
            project_starttime: pro.sYearMonth,
            project_endtime: pro.eYearMonth,
            project_description: pro.desc
        })),
        skills: store.skills.map(skill => ({
            skills: skill.name
        })),
        achievements: store.achievements.map(ach => ({
            achievement_name: ach.title,
            achievement_time: ach.yearMonth
        }))
    }

    try {
        const response = await fetch('http://localhost:8000/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(resumeData)
        })

        const result = await response.json()
        console.log(result)
    } catch (error) {
        console.log(error)
    }
}
</script>

<template>
    <section class="container">
        <h2>Build Your Resume</h2>

        <form @submit.prevent="submitForm">
            <AccordionItem title="Personal Info" defaultOpen>
                <div class="info">
                    <div class="input-grp">
                        <label for="f-name">First Name</label>
                        <input id="f-name" v-model="store.firstName" type="text" required>
                    </div>
                    <div class="input-grp">
                        <label for="l-name">Last Name</label>
                        <input id="l-name" v-model="store.lastName" type="text" required>
                    </div>
                    <div class="input-grp">
                        <label for="email">Email</label>
                        <input id="email" v-model="store.email" type="email" required>
                    </div>
                    <div class="input-grp">
                        <label for="phone">Phone</label>
                        <input id="phone" v-model="store.phone" type="tel">
                    </div>
                    <div class="input-grp">
                        <label for="address">Address</label>
                        <input id="address" v-model="store.address" type="text">
                    </div>
                    <div class="input-grp">
                        <label for="job">Job Title</label>
                        <input id="job" v-model="store.jobTitle" type="text" required>
                    </div>
                </div>

                <div class="contacts">
                    <h4>Contacts</h4>

                    <div v-for="(contact, index) in store.contacts" :key="index" class="dynamic-item">
                        <div class="items">
                            <div class="input-grp">
                                <label :for="'p-name-' + index">Platform Name</label>
                                <input :id="'p-name-' + index" v-model="contact.platform" type="text">
                            </div>
                            <div class="input-grp">
                                <label :for="'p-link-' + index">Profile Link</label>
                                <input :id="'p-link-' + index" v-model="contact.link" type="text">
                            </div>
                        </div>
                        <button type="button" class="delete-btn" @click="store.deleteContact(index)">Delete</button>
                    </div>

                    <button type="button" class="add-btn" @click="store.addContact">Add Contact</button>
                </div>
            </AccordionItem>

            <AccordionItem title="Education">
                <div v-for="(edu, index) in store.educations" :key="index" class="dynamic-item">
                    <div class="items">
                        <div class="input-grp">
                            <label :for="'school-' + index">School Name</label>
                            <input :id="'school-' + index" v-model="edu.school" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'degree-' + index">Degree</label>
                            <input :id="'degree-' + index" v-model="edu.degree" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'edu-start-' + index">Starting Time</label>
                            <input :id="'edu-start-' + index" v-model="edu.sYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'edu-end-' + index">Ending Time</label>
                            <input :id="'edu-end-' + index" v-model="edu.eYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'result-' + index">Result Type</label>
                            <select :id="'result-' + index" v-model="edu.resultType">
                                <option value="CGPA">CGPA</option>
                                <option value="GPA">GPA</option>
                            </select>
                        </div>
                        <div class="input-grp">
                            <label :for="'score-' + index">Score</label>
                            <input :id="'score-' + index" v-model="edu.score" type="number" step="0.01">
                        </div>
                    </div>

                    <button type="button" class="delete-btn" @click="store.deleteEducation(index)">Delete</button>
                </div>

                <button type="button" class="add-btn" @click="store.addEducation">Add Education</button>
            </AccordionItem>

            <AccordionItem title="Experience">
                <div v-for="(exp, index) in store.experiences" :key="index" class="dynamic-item">
                    <div class="items">
                        <div class="input-grp">
                            <label :for="'company-' + index">Company</label>
                            <input :id="'company-' + index" v-model="exp.company" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'role-' + index">Role</label>
                            <input :id="'role-' + index" v-model="exp.role" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'exp-start-' + index">Starting Time</label>
                            <input :id="'exp-start-' + index" v-model="exp.sYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'exp-end-' + index">Ending Time</label>
                            <input :id="'exp-end-' + index" v-model="exp.eYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'exp-desc-' + index">Description</label>
                            <textarea :id="'exp-desc-' + index" v-model="exp.desc" rows="3" />
                        </div>
                    </div>

                    <button type="button" class="delete-btn" @click="store.deleteExperience(index)">Delete</button>
                </div>

                <button type="button" class="add-btn" @click="store.addExperience">Add Experience</button>
            </AccordionItem>

            <AccordionItem title="Skills">
                <div v-for="(skill, index) in store.skills" :key="index" class="dynamic-item">
                    <div class="items">
                        <div class="input-grp">
                            <label :for="'skill-' + index">Skill</label>
                            <input :id="'skill-' + index" v-model="skill.name" type="text">
                        </div>
                    </div>

                    <button type="button" class="delete-btn" @click="store.deleteSkill(index)">Delete</button>
                </div>

                <button type="button" class="add-btn" @click="store.addSkill">Add Skill</button>
            </AccordionItem>

            <AccordionItem title="Projects">
                <div v-for="(pro, index) in store.projects" :key="index" class="dynamic-item">
                    <div class="items">
                        <div class="input-grp">
                            <label :for="'p-name-' + index">Project Name</label>
                            <input :id="'p-name-' + index" v-model="pro.name" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'p-link-' + index">Project Link</label>
                            <input :id="'p-link-' + index" v-model="pro.link" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'pro-start-' + index">Starting Time</label>
                            <input :id="'pro-start-' + index" v-model="pro.sYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'pro-end-' + index">Ending Time</label>
                            <input :id="'pro-end-' + index" v-model="pro.eYearMonth" type="month">
                        </div>
                        <div class="input-grp">
                            <label :for="'pro-desc-' + index">Description</label>
                            <textarea :id="'pro-desc-' + index" v-model="pro.desc" rows="3" />
                        </div>
                    </div>

                    <button type="button" class="delete-btn" @click="store.deleteProject(index)">Delete</button>
                </div>

                <button type="button" class="add-btn" @click="store.addProject">Add Project</button>
            </AccordionItem>

            <AccordionItem title="Achievements">
                <div v-for="(ach, index) in store.achievements" :key="index" class="dynamic-item">
                    <div class="items">
                        <div class="input-grp">
                            <label :for="'achievement-' + index">Achievement</label>
                            <input :id="'achievement-' + index" v-model="ach.title" type="text">
                        </div>
                        <div class="input-grp">
                            <label :for="'ach-time-' + index">Time</label>
                            <input :id="'ach-time-' + index" v-model="ach.yearMonth" type="month">
                        </div>
                    </div>

                    <button type="button" class="delete-btn" @click="store.deleteAchievement(index)">Delete</button>
                </div>

                <button type="button" class="add-btn" @click="store.addAchievement">Add Achievement</button>
            </AccordionItem>

            <button type="submit" class="submit-btn">Generate Resume</button>
        </form>
    </section>
</template>

<style scoped>
.container {
    width: clamp(0px, 100%, 900px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2em;
}

form {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.5em;
}

.info {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5em;
}

.input-grp {
    flex: 1 1 calc(50% - 0.5em);
    display: flex;
    flex-direction: column;
}

.contacts {
    margin-top: 1em;
    display: flex;
    flex-direction: column;
    gap: 1em;
}

.dynamic-item {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #bbb;
    border-radius: 3px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1em;
}

.items {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 0.5em;
}

label {
    color: #8c8c8c;
}

input,
textarea,
select {
    padding: 0.5em;
    border: 1px dotted #8c8c8c;
    border-radius: 3px;
    transition: border 0.3s ease;
}

input:focus,
textarea:focus,
select:focus {
    border: 1px solid black;
}

.delete-btn {
    background-color: rgb(244, 67, 54);
    color: white;
    transition: background-color 0.7s ease;
}

.delete-btn:hover {
    background-color: rgba(244, 67, 54, 0.8);
}

.add-btn {
    background-color: rgb(76, 175, 80);
    color: white;
    transition: background-color 0.7s ease;
}

.add-btn:hover {
    background-color: rgba(76, 175, 80, 0.8);
}

.submit-btn {
    margin-top: 1.5em;
    background-color: rgb(33, 150, 243);
    color: white;
    transition: background-color 0.7s ease;
}

.submit-btn:hover {
    background-color: rgba(33, 150, 243, 0.8);
    color: white;
}
</style>