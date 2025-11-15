<template>
    <header>
        <NuxtLink to="/">
            <h1>Resume Buildr</h1>
        </NuxtLink>
    </header>
</template>

<style scoped>
header {
    width: 100%;
    padding: 0.5em 1em;
    border-bottom: 1px solid #ccc;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 1em;
}

h1 {
    font-family: 'Doto', monospace;
    font-weight: 500;
}
</style>