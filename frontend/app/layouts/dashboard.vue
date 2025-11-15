<template>
    <div class="container">
        <main>
            <slot />
        </main>
    </div>
</template>

<style scoped>
.container {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex-grow: 1;
    width: 100%;
    padding: 2em 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3em;
}
</style>