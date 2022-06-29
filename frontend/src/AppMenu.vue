<template>
	<div class="layout-menu-wrapper" :class="{'layout-sidebar-active': sidebarActive}"
		@click="onMenuClick" @mouseover="onSidebarMouseOver" @mouseleave="onSidebarMouseLeave">
		<div class="menu-logo">

			<a href="#" class="logo">
				<img :src="'layout/images/logo-'+ (colorScheme === 'light' ? 'dark' : 'light') + '.png'">
			</a>

			<a href="#" class="app-name">
				<img :src="'layout/images/appname-'+ (colorScheme === 'light' ? 'dark' : 'light') + '.png'"/>
			</a>
			<a href="#" class="menu-pin" @click="onToggleMenu">
				<span v-if="isOverlay()" class="pi pi-times"></span>
				<span v-if="isSidebar() && !sidebarStatic && pinActive" class="pi pi-unlock"></span>
				<span v-if="isSidebar() && sidebarStatic && pinActive" class="pi pi-lock"></span>
			</a>
		</div>

		<div class="layout-menu-container">
			<AppSubmenu class="layout-menu" :items="model" :menuMode="menuMode" :menuActive="menuActive" :root="true" :parentMenuItemActive="true"
				@menu-click="onMenuClick" @menuitem-click="onMenuItemClick" @root-menuitem-click="onRootMenuItemClick"/>
		</div>

		<AppInlineMenu :menuMode="menuMode" :activeInlineProfile="activeInlineProfile" @change-inlinemenu="onChangeActiveInlineMenu"></AppInlineMenu>
	</div>
</template>

<script>
import AppSubmenu from './AppSubmenu';
import AppInlineMenu from './AppInlineMenu';

export default {
	name: 'AppMenu',
	emits: ['menu-click', 'menuitem-click', 'root-menuitem-click', 'sidebar-mouse-over', 'sidebar-mouse-leave', 'toggle-menu', 'change-inlinemenu'],
	props: {
		model: Array,
		menuMode: String,
		colorScheme: String,
		menuActive: {
            type: Boolean,
            default: false
        },
		activeInlineProfile: {
			type: Boolean,
			default: false
		},
		sidebarActive: {
			type: Boolean,
			default: false
		},
		sidebarStatic: {
			type: Boolean,
			default: false
		},
		pinActive: {
			type: Boolean,
			default: false
		}
	},
	components: {
		AppSubmenu,
		AppInlineMenu
	},
	methods: {
		onSidebarMouseOver() {
            this.$emit('sidebar-mouse-over');
        },
        onSidebarMouseLeave() {
            this.$emit('sidebar-mouse-leave');
        },
		onMenuClick(event) {
            this.$emit('menu-click', event);
        },
        onMenuItemClick(event) {
            this.$emit('menuitem-click', event);
        },
		onRootMenuItemClick(event) {
			this.$emit('root-menuitem-click', event);
		},
		onToggleMenu(event) {
            this.$emit('toggle-menu', event);
        },
		onChangeActiveInlineMenu() {
			this.$emit('change-inlinemenu');
		},
		isHorizontal() {
			return this.menuMode === 'horizontal';
		},
		isSlim() {
			return this.menuMode === 'slim';
		},
		isOverlay() {
			return this.menuMode === 'overlay';
		},
		isStatic() {
			return this.menuMode === 'static';
		},
		isSidebar() {
			return this.menuMode === 'sidebar';
		},
		isDesktop() {
			return window.innerWidth > 991;
		},
		isMobile() {
			return window.innerWidth <= 991;
		}
	}
}
</script>

<style scoped>

</style>