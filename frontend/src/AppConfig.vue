<template>
    <div id="layout-config">
        <a id="layout-config-button" class="layout-config-button" @click="onConfigButtonClick($event)">
            <i class="pi pi-cog"></i>
        </a>
        <div class="layout-config" :class="{ 'layout-config-active': configActive }" @click="onConfigClick">
            <h5>Menu Type</h5>
            <div class="field-radiobutton">
                <RadioButton name="menuMode" value="static" v-model="d_menuMode" id="mode1" @change="changeMenuMode('static')"></RadioButton>
                <label for="mode1">Static</label>
            </div>
            <div class="field-radiobutton">
                <RadioButton name="menuMode" value="overlay" v-model="d_menuMode" id="mode2" @change="changeMenuMode('overlay')"></RadioButton>
                <label for="mode2">Overlay</label>
            </div>
            <div class="field-radiobutton">
                <RadioButton name="menuMode" value="slim" v-model="d_menuMode" id="mode3" @change="changeMenuMode('slim')"></RadioButton>
                <label for="mode3">Slim</label>
            </div>
            <div class="field-radiobutton">
                <RadioButton name="menuMode" value="horizontal" v-model="d_menuMode" id="mode4" @change="changeMenuMode('horizontal')"></RadioButton>
                <label for="mode4">Horizontal</label>
            </div>
            <div class="field-radiobutton">
                <RadioButton name="menuMode" value="sidebar" v-model="d_menuMode" id="mode5" @change="changeMenuMode('sidebar')"></RadioButton>
                <label for="mode5">Sidebar</label>
            </div>
            <hr />

            <h5>Color Scheme</h5>
            <div class="field-radiobutton">
                <RadioButton name="colorScheme" value="light" v-model="d_colorScheme" id="theme1" @change="changeColorScheme('light')"></RadioButton>
                <label for="theme1">Light</label>
            </div>
            <div class="field-radiobutton">
                <RadioButton name="colorScheme" value="dark" v-model="d_colorScheme" id="theme2" @change="changeColorScheme('dark')"></RadioButton>
                <label for="theme2">Dark</label>
            </div>
            <hr />

            <h5>Ripple Effect</h5>
            <InputSwitch :modelValue="rippleActive" @update:modelValue="onRippleChange"  />
            <hr />

            <h5>Layouts</h5>
            <div class="layout-themes">
                <div v-for="t in themes" :key="t.name">
                    <a style="cursor: pointer" @click="changeTheme(t.name)" :title="t.name" :style="{ 'background-color': t.color }">
                        <i class="pi pi-check" v-if="theme === t.name"></i>
                    </a>
                </div>
            </div>
            <hr />

            <h5>Themes</h5>
            <div class="layout-themes">
                <div v-for="theme in componentThemes" :key="theme.name">
                    <a style="cursor: pointer" @click="changeComponentTheme(theme.name)" :title="theme.name" :style="{ 'background-color': theme.color }">
                        <i class="pi pi-check" v-if="componentTheme === theme.name"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AppConfig',
    emits: ['config-button-click', 'config-click', 'change-color-scheme', 'change-menu-theme', 'change-component-theme', 'change-menu-mode'],
    props: {
        configActive: {
            type: Boolean,
            default: null,
        },
        configClick: {
            type: Boolean,
            default: null,
        },
        colorScheme: String,
        theme: String,
        componentTheme: String,
        menuMode: String
    },
    data() {
        return {
            themes: [
                {name: 'blue', color: '#0F8BFD'},
                {name: 'green', color: '#0BD18A'},
                {name: 'magenta', color: '#EC4DBC'},
                {name: 'orange', color: '#FD9214'},
                {name: 'purple', color: '#873EFE'},
                {name: 'red', color: '#FC6161'},
                {name: 'teal', color: '#00D0DE'},
                {name: 'yellow', color: '#EEE500'}
            ],
            componentThemes: [
                {name: 'blue', color: '#0F8BFD'},
                {name: 'green', color: '#0BD18A'},
                {name: 'magenta', color: '#EC4DBC'},
                {name: 'orange', color: '#FD9214'},
                {name: 'purple', color: '#873EFE'},
                {name: 'red', color: '#FC6161'},
                {name: 'teal', color: '#00D0DE'},
                {name: 'yellow', color: '#EEE500'}
            ],
            d_colorScheme: this.colorScheme,
            d_menuMode: this.menuMode
        };
    },
    computed: {
        rippleActive() {
            return this.$primevue.config.ripple;
        }
    },
    methods: {
        changeTheme(theme) {
            this.$emit('change-menu-theme', theme);
        },
        changeComponentTheme(theme) {
            this.$emit('change-component-theme', theme);
        },
        changeColorScheme(scheme) {
            this.$emit('change-color-scheme', scheme);
        },
        onConfigButtonClick(event) {
            this.$emit('config-button-click', event);
            event.preventDefault();
        },
        onConfigClick(event) {
            this.$emit('config-click', event);
        },
        changeMenuMode(mode) {
            this.$emit('change-menu-mode', mode);
        },
        onRippleChange(value) {
            this.$primevue.config.ripple = value;
        }
    }
};
</script>
