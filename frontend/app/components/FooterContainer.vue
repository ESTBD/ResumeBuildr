<script setup>
const startYear = 2025;
const year = new Date().getFullYear();
</script>

<template>
    <footer>
        <section class="developers">
            <article>
                Frontend by <a href="https://github.com/Atia-Farha" target="_blank">Atia Farha</a>
            </article>
            
            <article>
                Backend by <a href="https://github.com/smsadat-dev" target="_blank">S.M. Nazmus Sadat</a>
            </article>
        </section>

        <section class="copyright">
            Copyright {{ startYear }}{{ year > startYear ? ' - ' + year : '' }}
            <NuxtLink to="/" class="brand-logo">Resume Buildr</NuxtLink>
        </section>
    </footer>
</template>

<style scoped>
footer {
    width: 100%;
    padding: 1em;
    border-top: 1px solid #ccc;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow-x: hidden;
    gap: 2em;
}

article,
a,
.copyright {
    font-family: 'Doto', monospace;
    font-weight: 500;
}

a {
    font-weight: 700;
}
</style>