<template>
	<div class="layout-topbar">
        <div class="layout-topbar-left">
            <a href="#" class="topbar-menu-button" @click="onMenuButtonClick($event)">
                <i class="pi pi-bars"></i>
            </a>

            <a href="#" class="logo">
                <img :src="'layout/images/logo-'+ (colorScheme === 'light' ? 'dark' : 'light') + '.png'">
            </a>

            <a href="#">
                <img :src="'layout/images/appname-'+ (colorScheme === 'light' ? 'dark' : 'light') + '.png'" class="app-name"/>
            </a>
        </div>

        <AppMenu :model="items" :menuMode="menuMode" :colorScheme="colorScheme" :menuActive="menuActive" :activeInlineProfile="activeInlineProfile"
            @sidebar-mouse-over="onSidebarMouseOver" @sidebar-mouse-leave="onSidebarMouseLeave" @toggle-menu="onToggleMenu" @change-inlinemenu="onChangeActiveInlineMenu" 
            @menu-click="onMenuClick" @root-menuitem-click="onRootMenuItemClick" @menuitem-click="onMenuItemClick" />

        <div class="layout-topbar-right">
            <ul class="layout-topbar-right-items">
                <li id="profile" class="profile-item" :class="{'active-topmenuitem': topbarMenuActive}">
                    <a href="#" @click="onTopbarItemClick($event, 'profile')">
                        <img src="layout/images/profile-image.png">
                    </a>

                    <ul class="fadeInDown">
                        <li role="menuitem">
                            <a href="#" @click="onTopbarSubItemClick($event)">
                                <i class="pi pi-fw pi-user"></i>
                                <span>Profile</span>
                            </a>
                        </li>
                        <li role="menuitem">
                            <a href="#" @click="onTopbarSubItemClick($event)">
                                <i class="pi pi-fw pi-cog"></i>
                                <span>Settings</span>
                            </a>
                        </li>
                        <li role="menuitem">
                            <a href="#" @click="onTopbarSubItemClick($event)">
                                <i class="pi pi-fw pi-sign-out"></i>
                                <span>Logout</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#">
                        <i class="topbar-icon pi pi-fw pi-bell"></i>
                        <span class="topbar-badge">2</span>
                        <span class="topbar-item-name">Notifications</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <i class="topbar-icon pi pi-fw pi-comment"></i>
                        <span class="topbar-badge">5</span>
                        <span class="topbar-item-name">Messages</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import AppMenu from './AppMenu.vue';
export default {
	emits: ['menu-click', 'menuitem-click', 'root-menuitem-click', 'menubutton-click', 'sidebar-mouse-over', 'sidebar-mouse-leave', 'toggle-menu', 'change-inlinemenu', 'topbar-item-click'],
	data() {
		return {
			activeTopbarItem: null
		}
	},
	props: {
        items: Array,
		menuMode: String,
		colorScheme: String,
        topbarMenuActive: {
            type: Boolean,
            default: false
        },
        menuActive: {
            type: Boolean,
            default: false
        },
        activeInlineProfile: {
            type: Boolean,
            default: false
        }
	},
	methods: {
        onMenuClick(event) {
            this.$emit('menu-click', event);
        },
        onMenuItemClick(event) {
            this.$emit('menuitem-click', event);
        },
        onRootMenuItemClick(event) {
            this.$emit('root-menuitem-click', event);
        },
		onMenuButtonClick(event) {
			this.$emit('menubutton-click', event);
		},
		onTopbarItemClick(event, item) {
            this.$emit('topbar-item-click', event, item);	
			event.preventDefault();
		},
		onTopbarSubItemClick(event) {
			event.preventDefault();
		},
        onSidebarMouseOver() {
            this.$emit('sidebar-mouse-over');
        },
        onSidebarMouseLeave() {
            this.$emit('sidebar-mouse-leave');
        },
        onToggleMenu(event) {
            this.$emit('toggle-menu', event);
        },
        onChangeActiveInlineMenu() {
            this.$emit('change-inlinemenu');
        },
		isOverlay() {
			return this.menuMode === 'overlay';
		}
	},
	components: {
		AppMenu
	}
}
</script>
