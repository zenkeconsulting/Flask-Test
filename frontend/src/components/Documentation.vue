<template>
    <div class="grid">
        <div class="col-12">
            <div class="card docs">
                <h4>Current Version</h4>
                <p>Vue 3 and PrimeVue 3.x</p>

                <h4>Dependencies</h4>
				<p>
					Atlantis has no direct dependency other than PrimeVue. More
					information about dependencies is available at
					<a href="https://www.primefaces.org/primevue-3-0-0-final-released-for-vue-3/">PrimeVue 3.0.0 Is Ready For PrimeTime</a>
					article.
				</p>

                <h4>Getting Started</h4>
                <p>Atlantis is an application template for Vue based on the <a href="https://www.primefaces.org/primevue-3-0-0-final-released-for-vue-3/">PrimeVue 3.0.0 Is Ready For PrimeTime</a>
					article.
                </p>
<pre v-code><code>
npm install -g @vue/cli

# OR

yarn global add @vue/cli

</code></pre>

                <p>Once CLI is ready in your system, extract the contents of the Atlantis zip file distribution, cd to the directory and install the libraries from npm.</p>

<pre v-code><code>
cd atlantis
npm install
npm run serve

</code></pre>

                <p>The application should run at http://localhost:8080/, you may now start with the development of your application.</p>

                <h4>Important CLI Commands</h4>
                <p>Following commands are derived from CLI.</p>
<pre v-code><code>
"npm run serve": Starts the development server
"npm run build": Builds the application for deployment.
"npm run lint": Executes the lint checks.
"npm run test:unit": Runs the tests.

</code></pre>

                <h4>Structure</h4>
                <p>Atlantis consists of 3 main parts; the application layout, layout resources and theme resources for PrimeVue components. <i>App.vue</i> inside src folder is the main component containing the template for the base layout
                    required resources for the layout are placed inside the <i>public/layout</i> folder and similarly theme resources are inside <i>public/theme</i> folder.</p>

                <h4>Template</h4>
                <p>Main layout is the template of the <i>App.vue</i>, it is divided into a couple of child components such as topbar, content, menu and footer. Here is template of the
                    <i>App.vue</i> component that implements the logic such as menu state, layout modes and other configurable options.
                </p>
<pre v-code><code>
&lt;template&gt;
	&lt;div :class="layoutContainerClass" @click="onDocumentClick"&gt;
		&lt;div class="layout-main"&gt;
			&lt;AppTopBar :items="menu" :menuMode="menuMode" :colorScheme="colorScheme" :menuActive="menuActive" :topbarMenuActive="topbarMenuActive" :activeInlineProfile="activeInlineProfile" 
				@topbar-item-click="onTopbarItemClick" @menubutton-click="onMenuButtonClick" @sidebar-mouse-over="onSidebarMouseOver" @sidebar-mouse-leave="onSidebarMouseLeave" @toggle-menu="onToggleMenu" @change-inlinemenu="onChangeActiveInlineMenu" 
				@menu-click="onMenuClick" @menuitem-click="onMenuItemClick" @root-menuitem-click="onRootMenuItemClick" /&gt;

			&lt;AppMenu :model="menu" :menuMode="menuMode" :colorScheme="colorScheme" :menuActive="menuActive" :sidebarActive="sidebarActive" :sidebarStatic="sidebarStatic" :pinActive="pinActive" :activeInlineProfile="activeInlineProfile"
				@sidebar-mouse-over="onSidebarMouseOver" @sidebar-mouse-leave="onSidebarMouseLeave" @toggle-menu="onToggleMenu" @change-inlinemenu="onChangeActiveInlineMenu" @menu-click="onMenuClick" @menuitem-click="onMenuItemClick" @root-menuitem-click="onRootMenuItemClick" /&gt;

			&lt;AppBreadcrumb :menuMode="menuMode" v-model:searchActive="searchActive" v-model:searchClick="searchClick" @menubutton-click="onMenuButtonClick" @rightmenu-button-click="onRightMenuButtonClick" /&gt;

			&lt;div class="layout-main-content"&gt;
				&lt;router-view /&gt;
			&lt;/div&gt;

			&lt;AppFooter :colorScheme="colorScheme" /&gt;
		&lt;/div&gt;

		&lt;AppRightMenu :rightMenuActive="rightMenuActive" @rightmenu-click="onRightMenuClick" @rightmenu-active="onChangeRightMenuActive" /&gt;

		&lt;AppConfig v-model:menuMode="menuMode" :theme="theme" :componentTheme="componentTheme" :colorScheme="colorScheme" :configActive="configActive" :configClick="configClick"
			@config-button-click="onConfigButtonClick" @config-click="onConfigClick" @change-color-scheme="onChangeColorScheme" @change-component-theme="onChangeComponentTheme" @change-menu-theme="onChangeMenuTheme"
			@change-menu-mode="onChangeMenuMode" /&gt;
	&lt;/div&gt;
&lt;/template&gt;

</code></pre>

                <h4>Menu</h4>
                <p>Menu is a separate component defined in <i>AppMenu.vue</i> file. In order to define the menuitems,
                    navigate to data section of <i>App.vue</i> file and define your own model as a nested structure using the menu property.
                    Here is the menu component from the demo application. Notice that menu object is bound to the model property of AppMenu component as shown above.</p>

<div style="overflow: auto; height: 400px; margin-bottom: 10px">
<pre v-code.script><code>
data() &#123;
    return &#123;
        menu: [
			{
				label: 'Favorites', 
				icon: 'pi pi-fw pi-home',
				items: [
					{label: 'Dashboard Sales', icon: 'pi pi-fw pi-home', to: '/'}
				]
			},
			{
				label: 'UI Kit', icon: 'pi pi-fw pi-star-fill',
				items: [
					{label: 'Input', icon: 'pi pi-fw pi-check-square', to: '/input'},
					{label: 'Float Label', icon: 'pi pi-fw pi-bookmark', to: '/floatlabel'},
					{label: 'Invalid State', icon: 'pi pi-fw pi-exclamation-circle', to: '/invalidstate'},
					{label: 'Button', icon: 'pi pi-fw pi-mobile', to: '/button', class: 'rotated-icon'},
					{label: 'Table', icon: 'pi pi-fw pi-table', to: '/table'},
					{label: 'List', icon: 'pi pi-fw pi-list', to: '/list'},
					{label: 'Tree', icon: 'pi pi-fw pi-share-alt', to: '/tree'},
					{label: 'Panel', icon: 'pi pi-fw pi-tablet', to: '/panel'},
					{label: 'Overlay', icon: 'pi pi-fw pi-clone', to: '/overlay'},
					{label: 'Media', icon: 'pi pi-fw pi-image', to: '/media'},
					{label: 'Menu', icon: 'pi pi-fw pi-bars', to: '/menus'},
					{label: 'Message', icon: 'pi pi-fw pi-comment', to: '/messages'},
					{label: 'File', icon: 'pi pi-fw pi-file', to: '/file'},
					{label: 'Chart', icon: 'pi pi-fw pi-chart-bar', to: '/chart'},
					{label: 'Misc', icon: 'pi pi-fw pi-circle-off', to: '/misc'},
				]
			},
			{
				label: 'Utilities', icon:'pi pi-fw pi-compass',
				items: [
					{label: 'Form Layout', icon: 'pi pi-fw pi-id-card', to: '/formlayout'},
					{label: 'Display', icon:'pi pi-fw pi-desktop', to:'/display'},
					{label: 'Elevation', icon:'pi pi-fw pi-external-link', to:'/elevation'},
					{label: 'Flexbox', icon:'pi pi-fw pi-directions', to:'/flexbox'},
					{label: 'Icons', icon:'pi pi-fw pi-prime', to:'/icons'},
					{label: 'Text', icon:'pi pi-fw pi-pencil', to:'/text'},
					{label: 'Widgets', icon:'pi pi-fw pi-star-fill', to:'/widgets'},
					{label: 'Grid System', icon:'pi pi-fw pi-th-large', to:'/grid'},
					{label: 'Spacing', icon:'pi pi-fw pi-arrow-right', to:'/spacing'},
					{label: 'Typography', icon:'pi pi-fw pi-align-center', to:'/typography'}
				]
			},
            {
                label: 'UI Blocks', icon: 'pi pi-fw pi-globe',
                items: [
                    {label: 'Free Blocks', icon: 'pi pi-fw pi-eye', to: '/blocks'},
                    {label: 'All Blocks', icon: 'pi pi-fw pi-globe', url: 'https://www.primefaces.org/primeblocks-vue'}
                ]
            },
			{
				label: 'Pages', icon: 'pi pi-fw pi-briefcase',
				items: [
					{label: 'Crud', icon: 'pi pi-fw pi-pencil', to: '/crud'},
					{label: 'Calendar', icon: 'pi pi-fw pi-calendar-plus', to: '/calendar'},
					{label: 'Timeline', icon: 'pi pi-fw pi-calendar', to: '/timeline'},
                    {label: 'Landing', icon: 'pi pi-fw pi-globe', url: 'pages/landing.html', target: '_blank'},
					{label: 'Login', icon: 'pi pi-fw pi-sign-in', to: '/login'},
					{label: 'Invoice', icon: 'pi pi-fw pi-dollar', to: '/invoice'},
					{label: 'Help', icon: 'pi pi-fw pi-question-circle', to: '/help'},
					{label: 'Error', icon: 'pi pi-fw pi-times-circle', to: '/error'},
					{label: 'Not Found', icon: 'pi pi-fw pi-exclamation-circle', to: '/notfound'},
					{label: 'Access Denied', icon: 'pi pi-fw pi-lock', to: '/access'},
					{label: 'Empty', icon: 'pi pi-fw pi-circle-off', to: '/empty'}
				]
			},
			{
				label: 'Hierarchy', icon: 'pi pi-fw pi-align-left',
				items: [
					{
						label: 'Submenu 1', icon: 'pi pi-fw pi-align-left',
						items: [
							{
								label: 'Submenu 1.1', icon: 'pi pi-fw pi-align-left',
								items: [
									{label: 'Submenu 1.1.1', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 1.1.2', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 1.1.3', icon: 'pi pi-fw pi-align-left'},
								]
							},
							{
								label: 'Submenu 1.2', icon: 'pi pi-fw pi-align-left',
								items: [
									{label: 'Submenu 1.2.1', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 1.2.2', icon: 'pi pi-fw pi-align-left'}
								]
							},
						]
					},
					{
						label: 'Submenu 2', icon: 'pi pi-fw pi-align-left',
						items: [
							{
								label: 'Submenu 2.1', icon: 'pi pi-fw pi-align-left',
								items: [
									{label: 'Submenu 2.1.1', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 2.1.2', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 2.1.3', icon: 'pi pi-fw pi-align-left'},
								]
							},
							{
								label: 'Submenu 2.2', icon: 'pi pi-fw pi-align-left',
								items: [
									{label: 'Submenu 2.2.1', icon: 'pi pi-fw pi-align-left'},
									{label: 'Submenu 2.2.2', icon: 'pi pi-fw pi-align-left'}
								]
							},
						]
					}
				]
			},
			{
				label: 'Start', icon: 'pi pi-fw pi-download',
				items: [
					{
						label: 'Buy Now', icon: 'pi pi-fw pi-shopping-cart', command: () => { window.location = 'https://www.primefaces.org/store'}
					},
					{
						label: 'Documentation', icon: 'pi pi-fw pi-info-circle', to: '/documentation'
					}
				]
			}
        ]
    &#125;
&#125;

</code></pre>
</div>

                <h4>Integration with an Existing CLI Project</h4>
				<p>To setup Atlantis in an existing project, follow the steps below;</p>

				<ul>
					<li>Copy the <i>public</i> and <i>src/assets</i> folder to your projects folder with the same name</li>
					<li>Copy all <i>src/App*.vue</i> files to the src folder of your application.</li>
				</ul>

				<p>Install PrimeVue</p>

<pre v-code><code>
npm install primevue@latest --save
npm install	primeicons@latest --save

</code></pre>

                <p>Add PrimeVue CSS at styles section in main.js.</p>

<pre v-code><code>
import 'primevue/resources/primevue.min.css';   	//required: PrimeVue components
import 'primeicons/primeicons.css';	 				//required: PrimeIcons
import './App.scss'; 	                            //your styles and overrides

</code></pre>

                <p>Last part is adding theme and layout css files, in the CLI app they are defined using link tags in index.html so the demo can switch them on the fly by changing the path however
                    if this is not a requirement, you may also add them to the styles configuration above so they go inside the bundle.</p>

                <h4>Integration with an Existing Non-CLI Project</h4>
                <p>For an existing project that do not use CLI, setup steps are more or less similar. Start with installing the dependencies listed above in package.json</p>
                <p>Copy the <i>src/assets</i> folder to your application and include the resources listed above with a module bundler like webpack or using link-script tags.</p>
                <p>Finally copy the contents of App.vue to your application's main component template such as <i>app/index.html</i> along
                    with the sub components which are AppMenu.vue, AppTopbar.vue and AppFooter.vue.</p>

                <h4>Theme</h4>
                <p>Atlantis provides 8 PrimeVue themes out of the box, setup of a theme simple including the css of theme to your page that are located inside theme folder.</p>
                <ul>
                    <li>theme-blue</li>
                    <li>theme-green</li>
                    <li>theme-magenta</li>
                    <li>theme-orange</li>
                    <li>theme-purple</li>
                    <li>theme-red</li>
                    <li>theme-teal</li>
                    <li>theme-yellow</li>
                </ul>

                <p>A custom theme can be developed by the following steps.</p>
                <ul>
                    <li>Choose a custom theme name such as theme-myown.</li>
                    <li>Create a file named theme-myown.scss under <i>public/theme folder</i>.</li>
                    <li>Define the variables listed below and import the <i>/sass/theme/_theme_light.scss</i> file.</li>
                    <li>Build the scss to generate css.</li>
                    <li>Include the theme file to your application.</li>
                </ul>

                <p>Here are the variables required to create a theme, you may need to change the last line according to the relative path of the sass folder in your application.</p>

<pre v-code.css><code>
$primaryColor: #0F8BFD;
$primaryLightColor: scale-color($primaryColor, $lightness: 60%) !default;
$primaryDarkColor: scale-color($primaryColor, $lightness: -10%) !default;
$primaryDarkerColor: scale-color($primaryColor, $lightness: -20%) !default;
$primaryTextColor: #ffffff;

$highlightBg: $primaryColor;
$highlightTextColor: $primaryTextColor;

@import '../../../src/assets/sass/theme/_theme_dark';

</code></pre>

                <p>If you prefer to compile manually, an example sass command to compile the css would be;</p>

<pre v-code><code>
sass public/theme-myown/theme.scss:public/theme-myown/theme.css

</code></pre>

                <p>Watch mode is handy to avoid compiling everytime when a change is made, instead use the following command
                so that sass generates the file whenever you make a customization. This builds all css files whenever a change is made to any scss file.</p>
<pre v-code><code>
sass --update public/layout/css/:public/layout/css/
sass --update public/theme/:public/theme/

</code></pre>

                <p>Same can also be applied to layout itself;</p>
                <ul>
                    <li>Choose a layout name such as layout-myown.</li>
                    <li>Create a file named layout-myown.scss under <i>layout/css folder</i>.</li>
                    <li>Define the variables listed below and import the <i>/sass/layout/_layout_light.scss</i> file.</li>
                    <li>Build the scss to generate css.</li>
                    <li>Serve the css by importing it using a link tag or a bundler.</li>
                </ul>

                <p>Here are the variables required to create a layout, you may need to change the last line according to the relative path of the sass folder in your application.</p>
<pre v-code.css><code>
$primaryColor: #0F8BFD;
$primaryTextColor: #ffffff;

@import '../../../../src/assets/sass/layout/_layout_dark';

</code></pre>

                <p>For both cases, several .scss files such as _layout.scss, _theme.scss or _variables.scss has to be present relative to your scss files, these are available inside the sass folder in the distribution.</p>
                <p>In case you'd like to customize the structure not just the colors, the _variables.scss is where the structural variables (e.g. font size, paddings) for the layout are defined.</p>

                <h5>assets/sass/variables/layout/_common.scss</h5>
<pre v-code.css><code>
//general
$fontSize:14px !default;
$fontFamily:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !default;
$transitionDuration:.2s !default;
$animationDuration:.4s !default;
$animationTimingFunction:cubic-bezier(.05,.74,.2,.99) !default;
$letterSpacing:normal !default;
$borderRadius:8px !default;
$tabletBreakpoint:991px !default;
$phoneBreakpoint:576px !default;

</code></pre>

                <h5>assets/sass/variables/theme/_theme_dark.scss</h5>
<div style="height:400px;overflow: auto;">
<pre v-code.css><code>
$colors: (
    "blue": #2196F3,
    "green": #4caf50,
    "yellow": #FBC02D,
    "cyan": #00BCD4,
    "pink": #E91E63,
    "indigo": #3F51B5,
    "teal": #009688,
    "orange": #F57C00,
    "bluegray": #607D8B,
    "purple": #9C27B0
);

//shades
$shade000:#FFFFFF!default;  //text color
$shade100:#C8CCD8 !default;  //text secondary color
$shade200:#868C9B !default;  //text third color
$shade500:rgba(255, 255, 255, 0.05) !default; //Alpha-01
$shade600:rgba(255, 255, 255, 0.1) !default;  //Alpha-02
$shade700:rgba(255, 255, 255, 0.15) !default;  //Alpha-03
$shade800:rgba(255, 255, 255, 0.2) !default;  //Alpha-04
$shade900:rgba(255, 255, 255, 0.25) !default;  //Alpha-05

$solidSurfaceColor: #0a061a;
$hoverBg:rgba(255,255,255,.03) !default;

//global
$fontFamily:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !default;
$fontSize:1rem !default;
$fontWeight:normal !default;
$textColor:$shade000 !default;
$textSecondaryColor:$shade100 !default;
$borderRadius:6px !default;
$transitionDuration:.2s !default;
$formElementTransition:background-color $transitionDuration, color $transitionDuration, border-color $transitionDuration, box-shadow $transitionDuration !default;
$actionIconTransition:background-color $transitionDuration, color $transitionDuration, box-shadow $transitionDuration !default;
$listItemTransition: box-shadow $transitionDuration !default;
$primeIconFontSize:1rem !default;
$divider:1px solid $shade500 !default;
$inlineSpacing:.5rem !default; //spacing between inline elements
$disabledOpacity:.4 !default; //opacity of a disabled item
$maskBg:rgba(0, 0, 0, 0.4) !default; //modal mask bg color
$loadingIconFontSize:2rem !default;
$errorColor:#FC6161 !default;

//scale
$scaleSM:0.875 !default;
$scaleLG:1.25 !default;

//focus
$focusOutlineColor:$primaryColor !default;
$focusOutline:0 none !default;
$focusOutlineOffset:0 !default;
$focusShadow:0 none !default;

//action icons
$actionIconWidth: 2rem !default;
$actionIconHeight: 2rem !default;
$actionIconBg: transparent !default;
$actionIconBorder: 0 none !default;
$actionIconColor: $shade100 !default;
$actionIconHoverBg: $shade500 !default;
$actionIconHoverBorderColor: transparent !default;
$actionIconHoverColor: $shade000 !default;
$actionIconBorderRadius: 50% !default;

//input field (e.g. inputtext, spinner, inputmask)
$inputPadding:0.429rem 0.571rem !default;
$inputTextFontSize:1rem !default;
$inputBg:$shade500 !default;
$inputTextColor:$shade000 !default;
$inputIconColor:$shade100 !default;
$inputBorder:1px solid transparent !default;
$inputHoverBorderColor:transparent !default;
$inputFocusBorderColor:$primaryColor !default;
$inputErrorBorderColor:$errorColor !default;
$inputPlaceholderTextColor:$shade200 !default;
$inputFilledBg:$shade500 !default;      //??
$inputFilledHoverBg:$inputFilledBg !default;
$inputFilledFocusBg:$inputFilledBg !default;

//input groups
$inputGroupBg:$shade500 !default;
$inputGroupTextColor:$shade100 !default;
$inputGroupAddOnMinWidth:2.357rem !default;

//input lists (e.g. dropdown, autocomplete, multiselect, orderlist)
$inputListBg:$shade500 !default;
$inputListTextColor:$shade000 !default;
$inputListBorder:$inputBorder !default;
$inputListPadding:0.286rem !default;
$inputListItemPadding:0.429rem 0.286rem !default;
$inputListItemBg:transparent !default;
$inputListItemTextColor:$shade000 !default;
$inputListItemHoverBg:$shade500 !default;
$inputListItemTextHoverColor:$shade000 !default;
$inputListItemBorder:0 none !default;
$inputListItemBorderRadius:4px !default;
$inputListItemMargin:0 !default;
$inputListItemFocusShadow:0 none !default;
$inputListHeaderPadding:0.429rem 0.286rem !default;
$inputListHeaderMargin:0 !default;
$inputListHeaderBg:$shade500 !default;
$inputListHeaderTextColor:$shade000 !default;
$inputListHeaderBorder:0 none !default;

//inputs with overlays (e.g. autocomplete, dropdown, multiselect)
$inputOverlayBg:$solidSurfaceColor !default;
$inputOverlayHeaderBg:$inputListHeaderBg !default;
$inputOverlayBorder:0 none !default;
$inputOverlayShadow:0 2px 4px -1px rgba(0,0,0,.2), 0 4px 5px 0 rgba(0,0,0,.14), 0 1px 10px 0 rgba(0,0,0,.12) !default;

//password
$passwordPanelBg:$solidSurfaceColor !default;
$passwordMeterBg:$shade600 !default;
$passwordWeakBg:#F48FB1 !default;
$passwordMediumBg:#FFE082 !default;
$passwordStrongBg:#C5E1A5 !default;

//button
$buttonPadding:0.429rem 0.571rem !default;
$buttonIconOnlyWidth:2.286rem !default;
$buttonIconOnlyPadding:0.429rem 0 !default;
$buttonBg:$primaryColor !default;
$buttonTextColor:$primaryTextColor !default;
$buttonBorder:1px solid $primaryColor !default;
$buttonHoverBg:$primaryDarkColor !default;
$buttonTextHoverColor:$primaryTextColor !default;
$buttonHoverBorderColor:$primaryDarkColor !default;
$buttonActiveBg:$primaryDarkerColor !default;
$buttonTextActiveColor:$primaryTextColor !default;
$buttonActiveBorderColor:$primaryDarkerColor !default;
$buttonShadow: 0px 0px 10px rgba($primaryColor, 0.3) !default;

$selectbuttonShadow: none !default;
$raisedButtonShadow:0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12) !default;
$roundedButtonBorderRadius:2rem !default;

$textButtonHoverBgOpacity:.04 !default;
$textButtonActiveBgOpacity:.16 !default;
$outlinedButtonBorder:1px solid !default;
$plainButtonTextColor:$textSecondaryColor !default;
$plainButtonHoverBgColor:$shade500 !default;
$plainButtonActiveBgColor:rgba(255,255,255,.16) !default;

$secondaryButtonBg:$shade500 !default;
$secondaryButtonTextColor:#FFFFFF !default;
$secondaryButtonBorder:1px solid transparent !default;
$secondaryButtonHoverBg:$shade600 !default;
$secondaryButtonTextHoverColor:$secondaryButtonTextColor !default;
$secondaryButtonHoverBorderColor:transparent !default;
$secondaryButtonActiveBg:$shade700 !default;
$secondaryButtonTextActiveColor:$secondaryButtonTextColor !default;
$secondaryButtonActiveBorderColor:transparent !default;
$secondaryButtonShadow:none !default;
$secondaryButtonFocusShadow:none !default;

$infoButtonBg:#873EFE !default;
$infoButtonTextColor:#FFFFFF !default;
$infoButtonBorder:1px solid transparent !default;
$infoButtonHoverBg:#6C1AF2 !default;
$infoButtonTextHoverColor:$infoButtonTextColor !default;
$infoButtonHoverBorderColor:transparent !default;
$infoButtonActiveBg:#5310C1 !default;
$infoButtonTextActiveColor:$infoButtonTextColor !default;
$infoButtonActiveBorderColor:transparent !default;
$infoButtonShadow:0px 0px 10px rgba(135, 62, 254, 0.3) !default;
$infoButtonFocusShadow:none !default;

$successButtonBg:#0BD18A !default;
$successButtonTextColor:#FFFFFF !default;
$successButtonBorder:1px solid transparent !default;
$successButtonHoverBg:#049B65 !default;
$successButtonTextHoverColor:$successButtonTextColor !default;
$successButtonHoverBorderColor:transparent !default;
$successButtonActiveBg:#017E52 !default;
$successButtonTextActiveColor:$successButtonTextColor !default;
$successButtonActiveBorderColor:transparent !default;
$successButtonShadow:0px 0px 10px rgba(11, 209, 138, 0.3) !default;
$successButtonFocusShadow:none !default;

$warningButtonBg:#EEE500 !default;
$warningButtonTextColor:#2E323F !default;
$warningButtonBorder:1px solid transparent !default;
$warningButtonHoverBg:#D1C901 !default;
$warningButtonTextHoverColor:$warningButtonTextColor !default;
$warningButtonHoverBorderColor:transparent !default;
$warningButtonActiveBg:#BAB302 !default;
$warningButtonTextActiveColor:$warningButtonTextColor !default;
$warningButtonActiveBorderColor:transparent !default;
$warningButtonShadow:0px 0px 10px rgba(238, 229, 0, 0.3) !default;
$warningButtonFocusShadow:none !default;

$helpButtonBg:#EC4DBC !default;
$helpButtonTextColor:#FFFFFF !default;
$helpButtonBorder:1px solid transparent !default;
$helpButtonHoverBg:#E80EA6 !default;
$helpButtonTextHoverColor:$helpButtonTextColor !default;
$helpButtonHoverBorderColor:transparent !default;
$helpButtonActiveBg:#B30C81 !default;
$helpButtonTextActiveColor:$helpButtonTextColor !default;
$helpButtonActiveBorderColor:transparent !default;
$helpButtonShadow: 0px 0px 10px rgba(236, 77, 188, 0.3) !default;
$helpButtonFocusShadow:none !default;

$dangerButtonBg:#FC6161 !default;
$dangerButtonTextColor:#FFFFFF !default;
$dangerButtonBorder:1px solid transparent !default;
$dangerButtonHoverBg:#E73A3A !default;
$dangerButtonTextHoverColor:$dangerButtonTextColor !default;
$dangerButtonHoverBorderColor:transparent !default;
$dangerButtonActiveBg:#C42424 !default;
$dangerButtonTextActiveColor:$dangerButtonTextColor !default;
$dangerButtonActiveBorderColor:transparent !default;
$dangerButtonShadow:0px 0px 10px rgba(252, 97, 97, 0.3) !default;
$dangerButtonFocusShadow:none !default;

$linkButtonColor:$primaryColor !default;
$linkButtonHoverColor:$primaryColor !default;
$linkButtonTextHoverDecoration:underline !default;
$linkButtonFocusShadow:none !default;

//checkbox
$checkboxWidth:20px !default;
$checkboxHeight:20px !default;
$checkboxBorder:2px solid $shade800 !default;
$checkboxIconFontSize:14px !default;
$checkboxHoverBorderColor: $shade900 !default;
$checkboxActiveBorderColor:$primaryColor !default;
$checkboxActiveBg:$primaryColor !default;
$checkboxIconActiveColor:$primaryTextColor !default;
$checkboxActiveHoverBg:$primaryDarkerColor !default;
$checkboxIconActiveHoverColor:$primaryTextColor !default;
$checkboxActiveHoverBorderColor:$primaryDarkerColor !default;

//radiobutton
$radiobuttonWidth:20px !default;
$radiobuttonHeight:20px !default;
$radiobuttonBorder:2px solid #868C9B !default;
$radiobuttonIconSize:12px !default;
$radiobuttonHoverBorderColor: #C8CCD8 !default;
$radiobuttonActiveBorderColor:$primaryColor !default;
$radiobuttonActiveBg:$primaryColor !default;
$radiobuttonIconActiveColor:$primaryTextColor !default;
$radiobuttonActiveHoverBg:$primaryDarkerColor !default;
$radiobuttonIconActiveHoverColor:$primaryTextColor !default;
$radiobuttonActiveHoverBorderColor:$primaryDarkerColor !default;

//colorpicker
$colorPickerPreviewWidth:2rem !default;
$colorPickerPreviewHeight:2rem !default;
$colorPickerBg:$shade800 !default;
$colorPickerBorder:1px solid $shade600 !default;
$colorPickerHandleColor:$shade000 !default;

//togglebutton
$toggleButtonBg:$shade500 !default;
$toggleButtonBorder:1px solid transparent !default;
$toggleButtonTextColor:$shade000 !default;
$toggleButtonIconColor:$shade100 !default;
$toggleButtonHoverBg:$shade600 !default;
$toggleButtonHoverBorderColor:transparent !default;
$toggleButtonTextHoverColor:$shade000 !default;
$toggleButtonIconHoverColor:$shade100 !default;
$toggleButtonActiveBg:$primaryColor !default;
$toggleButtonActiveBorderColor:$primaryColor !default;
$toggleButtonTextActiveColor:$primaryTextColor !default;
$toggleButtonIconActiveColor:$primaryTextColor !default;
$toggleButtonActiveHoverBg:$primaryDarkColor !default;
$toggleButtonActiveHoverBorderColor:$primaryDarkColor !default;
$toggleButtonTextActiveHoverColor:$primaryTextColor !default;
$toggleButtonIconActiveHoverColor:$primaryTextColor !default;

//inplace
$inplacePadding:$inputPadding !default;
$inplaceHoverBg:$shade500 !default;
$inplaceTextHoverColor:$shade000 !default;

//rating
$ratingIconFontSize:1.286rem !default;
$ratingCancelIconColor:#FC6161 !default;
$ratingCancelIconHoverColor:#FC6161 !default;
$ratingStarIconOffColor:$shade000 !default;
$ratingStarIconOnColor:$primaryColor !default;
$ratingStarIconHoverColor:$primaryColor !default;

//slider
$sliderBg:$shade600 !default;
$sliderBorder:0 none !default;
$sliderHorizontalHeight:0.429rem !default;
$sliderVerticalWidth:0.429rem !default;
$sliderHandleWidth:1.143rem !default;
$sliderHandleHeight:1.143rem !default;
$sliderHandleBg:#ffffff !default;
$sliderHandleBorder:4px solid $primaryColor !default;
$sliderHandleBorderRadius:50% !default;
$sliderHandleHoverBorderColor:$primaryColor !default;
$sliderHandleHoverBg:$primaryColor !default;
$sliderRangeBg:$primaryColor !default;

//calendar
$calendarTableMargin:.5rem 0 !default;
$calendarPadding:0.857rem !default;
$calendarBg:$solidSurfaceColor !default;
$calendarInlineBg:transparent !default;
$calendarTextColor:$shade000 !default;
$calendarBorder:$inputListBorder !default;
$calendarOverlayBorder:$inputOverlayBorder !default;

$calendarHeaderPadding:0 0 .75rem 0 !default;
$calendarHeaderBg:transparent !default;
$calendarInlineHeaderBg:$calendarInlineBg !default;
$calendarHeaderBorder:0 none !default;
$calendarHeaderTextColor:$shade000 !default;
$calendarHeaderFontWeight:400 !default;
$calendarHeaderCellPadding:0.357rem !default;
$calendarHeaderCellFontWeight:500 !default;
$calendarHeaderCellFontSize:12px !default;
$calendarHeaderCellTextColor:$shade200 !default;
$calendarMonthYearHeaderHoverTextColor: $primaryColor !default;

$calendarCellDateBg: $shade500 !default;
$calendarCellDatePadding:0.357rem !default;
$calendarCellDateWidth:2.571rem !default;
$calendarCellDateHeight:2.571rem !default;
$calendarCellDateBorderRadius:$borderRadius!default;
$calendarCellDateBorder:2px solid transparent !default;
$calendarCellDateHoverBg:$shade600 !default;
$calendarCellDateTodayBg:$shade500 !default;
$calendarCellDateTodayBorderColor:$shade900 !default;
$calendarCellDateTodayTextColor:$shade000 !default;

$calendarButtonBarPadding:1rem 0 !default;
$calendarTimePickerPadding:.5rem !default;
$calendarTimePickerElementPadding:0 .5rem !default;
$calendarTimePickerTimeFontSize:1.25rem !default;

$calendarBreakpoint:769px !default;
$calendarCellDatePaddingSM:0 !default;

//input switch
$inputSwitchWidth:2.714rem !default;
$inputSwitchHeight:1.429rem !default;
$inputSwitchBorderRadius:12px !default;
$inputSwitchHandleWidth:1.143rem !default;
$inputSwitchHandleHeight:1.143rem !default;
$inputSwitchHandleBorderRadius:8px !default;
$inputSwitchSliderPadding:.25rem !default;
$inputSwitchSliderOffBg:$shade500 !default;
$inputSwitchHandleOffBg:$shade100 !default;
$inputSwitchSliderOffHoverBg:$shade600 !default;
$inputSwitchSliderOnBg:$primaryColor !default;
$inputSwitchSliderOnHoverBg:$primaryDarkColor !default;
$inputSwitchHandleOnBg:$shade000 !default;

//panel
$panelHeaderBorderColor: $shade700 !default;
$panelHeaderBorder:1px solid $shade700 !default;
$panelHeaderBg:transparent !default;
$panelHeaderTextColor:$shade000 !default;
$panelHeaderFontWeight:500 !default;
$panelHeaderPadding:0.714rem 1.143rem !default;
$panelToggleableHeaderPadding:0.429rem 0.571rem !default;

$panelHeaderHoverBg:$shade500 !default;
$panelHeaderHoverBorderColor:$shade700 !default;
$panelHeaderTextHoverColor:$shade000 !default;

$panelContentBorderColor: $shade700 !default;
$panelContentBorder:1px solid $shade700 !default;
$panelContentBg:transparent !default;
$panelContentTextColor:$shade000 !default;
$panelContentPadding:1.143rem !default;

$panelFooterBorder:1px solid $shade700 !default;
$panelFooterBg:transparent !default;
$panelFooterTextColor:$shade000 !default;
$panelFooterPadding:0.714rem 1.143rem !default;

$fieldsetContentPadding: 0.429rem !default;

//accordion
$accordionSpacing:0 !default;
$accordionHeaderBorder:$panelHeaderBorder !default;
$accordionHeaderBg:$panelHeaderBg !default;
$accordionHeaderTextColor:$panelHeaderTextColor !default;
$accordionHeaderFontWeight:$panelHeaderFontWeight !default;
$accordionHeaderPadding:$panelHeaderPadding !default;

$accordionHeaderHoverBg:$shade500 !default;
$accordionHeaderHoverBorderColor:$shade500 !default;
$accordionHeaderTextHoverColor:$shade000 !default;

$accordionHeaderActiveBg:$shade700 !default;
$accordionHeaderActiveBorderColor:$shade500 !default;
$accordionHeaderTextActiveColor:$shade000 !default;

$accordionHeaderActiveHoverBg:$shade700 !default;
$accordionHeaderActiveHoverBorderColor:$shade500 !default;
$accordionHeaderTextActiveHoverColor:$shade000 !default;

$accordionContentBorder:$panelContentBorder !default;
$accordionContentBg:$panelContentBg !default;
$accordionContentTextColor:$panelContentTextColor !default;
$accordionContentPadding:$panelContentPadding !default;

//tabview
$tabviewNavBorder:1px solid $shade700 !default;
$tabviewNavBorderWidth:0 0 2px 0 !default;
$tabviewNavBg:transparent !default;

$tabviewHeaderSpacing:0.857rem !default;
$tabviewHeaderBorder:solid transparent !default;
$tabviewHeaderBorderWidth:0 0 2px 0 !default;
$tabviewHeaderBorderColor:transparent transparent transparent transparent !default;
$tabviewHeaderBg:transparent !default;
$tabviewHeaderTextColor:$shade200 !default;
$tabviewHeaderFontWeight:$panelHeaderFontWeight !default;
$tabviewHeaderPadding:0.571rem 0.429rem !default;
$tabviewHeaderMargin:0 0 -2px 0 !default;

$tabviewHeaderHoverBg:transparent !default;
$tabviewHeaderHoverBorderColor:$shade000 !default;
$tabviewHeaderTextHoverColor:$shade000 !default;

$tabviewHeaderActiveBg:transparent !default;
$tabviewHeaderActiveBorderColor:$primaryColor !default;
$tabviewHeaderTextActiveColor:$primaryColor !default;

$tabviewContentBorder:0 none !default;
$tabviewContentBg:transparent !default;
$tabviewContentTextColor:$shade000 !default;
$tabviewContentPadding:1.143rem 0 !default;

//upload
$fileUploadProgressBarHeight:.25rem !default;
$fileUploadContentPadding:2rem 1rem !default;

//scrollpanel
$scrollPanelTrackBorder:0 none !default;
$scrollPanelTrackBg:$shade500 !default;

//card
$cardBodyPadding:0.857rem 1.143rem !default;
$cardTitleFontSize:1.143rem !default;
$cardTitleFontWeight:500 !default;
$cardSubTitleFontSize:12px !default;
$cardSubTitleFontWeight:500 !default;
$cardSubTitleColor:$shade200 !default;
$cardContentPadding:1rem 0 !default;
$cardFooterPadding:1rem 0 0 0 !default;
$cardShadow:0 2px 1px -1px rgba(0,0,0,.2), 0 1px 1px 0 rgba(0,0,0,.14), 0 1px 3px 0 rgba(0,0,0,.12) !default;

//editor
$editorToolbarBg:$panelHeaderBg !default;
$editorToolbarBorder:$panelHeaderBorder !default;
$editorToolbarPadding:$panelHeaderPadding !default;
$editorToolbarIconColor:$textSecondaryColor !default;
$editorToolbarIconHoverColor:$textColor !default;
$editorIconActiveColor:$primaryColor !default;
$editorContentBorder:$panelContentBorder !default;
$editorContentBg:$panelContentBg !default;

//paginator
$paginatorBg:transparent !default;
$paginatorTextColor:$shade000 !default;
$paginatorBorder:solid $shade700 !default;
$paginatorBorderWidth:0 !default;
$paginatorPadding:.571rem .571rem !default;
$paginatorElementWidth:1.429rem !default;
$paginatorElementHeight:1.429rem !default;
$paginatorElementBg:transparent !default;
$paginatorElementBorder:0 none !default;
$paginatorElementIconColor:$shade000 !default;
$paginatorElementHoverBg:$shade500 !default;
$paginatorElementHoverBorderColor:transparent !default;
$paginatorElementIconHoverColor:$shade000 !default;
$paginatorElementActiveBg:$shade600 !default;
$paginatorElementActiveBorderColor:transparent !default;
$paginatorElementIconActiveColor:$shade000 !default;
$paginatorElementBorderRadius:4px !default;
$paginatorElementMargin:.143rem !default;
$paginatorElementPadding:0 !default;

//table
$tableHeaderBorder:1px solid $shade700 !default;
$tableHeaderBorderWidth:0 0 1px 0 !default;
$tableHeaderBg:transparent !default;
$tableHeaderTextColor:$shade200 !default;
$tableHeaderFontWeight:500 !default;
$tableHeaderPadding:0.571rem 0.571rem !default;

$tableHeaderCellPadding:0.571rem 0.571rem !default;
$tableHeaderCellBg:transparent !default;
$tableHeaderCellTextColor:$shade200 !default;
$tableHeaderCellFontWeight:500 !default;
$tableHeaderCellBorder:1px solid $shade700 !default;
$tableHeaderCellBorderWidth:0 0 1px 0 !default;
$tableHeaderCellHoverBg:$shade500 !default;
$tableHeaderCellTextHoverColor:$shade200 !default;
$tableHeaderCellIconColor:$shade200 !default;
$tableHeaderCellIconHoverColor:$shade200 !default;
$tableHeaderCellHighlightBg:$shade600 !default;
$tableHeaderCellHighlightTextColor:$shade200 !default;
$tableHeaderCellHighlightHoverBg:$shade600 !default;
$tableHeaderCellHighlightTextHoverColor:$shade200 !default;
$tableSortableColumnBadgeSize:1.143rem !default;

$tableBodyRowBg:transparent !default;
$tableBodyRowTextColor:$shade000 !default;
$tableBodyRowEvenBg:transparent !default;
$tableBodyRowHoverBg:$shade500 !default;
$tableBodyRowTextHoverColor:$shade000 !default;
$tableBodyRowHighlightBg: linear-gradient(0deg, rgba($highlightBg, 0.25), rgba($highlightBg, 0.25)), rgba(255, 255, 255, 0.05);
$tableBodyRowHighlightTextColor: $shade000;
$tableBodyCellBorder:1px solid $shade700 !default;
$tableBodyCellBorderWidth:0 0 0 0 !default;
$tableBodyCellPadding:0.429rem 0.571rem !default;

$tableFooterCellPadding:0.571rem 0.571rem !default;
$tableFooterCellBg:transparent !default;
$tableFooterCellTextColor:$shade200 !default;
$tableFooterCellFontWeight:500 !default;
$tableFooterCellBorder:1px solid  $shade700  !default;
$tableFooterCellBorderWidth:0 0 1px 0 !default;
$tableResizerHelperBg:$primaryColor !default;

$tableFooterBorder:1px solid  $shade700  !default;
$tableFooterBorderWidth:0 0 1px 0 !default;
$tableFooterBg:transparent !default;
$tableFooterTextColor:$shade200 !default;
$tableFooterFontWeight:500 !default;
$tableFooterPadding:0.571rem 0.571rem !default;

$tableCellContentAlignment:left !default;
$tableTopPaginatorBorderWidth:1px 0 1px 0 !default;
$tableBottomPaginatorBorderWidth:1px 0 1px 0 !default;

$tableScaleSM:0.5 !default;
$tableScaleLG:1.25 !default;

//dataview
$dataViewContentPadding:0 !default;
$dataViewContentBorder:0 none !default;
$dataViewListItemBorder:solid $shade500 !default;
$dataViewListItemBorderWidth:0 0 0 0 !default;

//orderlist
$orderlistBg:$shade500 !default;
$orderlistShadow:none !default;
$orderlistBorderRadius:8px !default;
$orderlistBorder:0 none !default;
$orderlistBorderWidth:0 0 0 0 !default;
$orderlistHeaderPadding:1.143rem !default;
$orderlistListPadding:0.571rem !default;
$orderlistListItemPadding:0.714rem 0.571rem !default;
$orderlistListItemBorder:1px solid transparent !default;
$orderlistListItemActiveBg:linear-gradient(0deg, rgba($highlightBg, 0.25), rgba($highlightBg, 0.25)), rgba(255, 255, 255, 0.05) !default;
$orderlistListItemActiveBorderColor:$highlightBg !default;

//picklist
$picklistBg:$shade500 !default;
$picklistShadow:none !default;
$picklistBorderRadius:8px !default;
$picklistBorder:0 none !default;
$picklistBorderWidth:0 0 0 0 !default;
$picklistHeaderPadding:1.143rem !default;
$picklistListPadding:0.571rem !default;
$picklistListItemPadding:0.714rem 0.571rem !default;
$picklistListItemBorder:1px solid transparent !default;
$picklistListItemActiveBg:linear-gradient(0deg, rgba($highlightBg, 0.25), rgba($highlightBg, 0.25)), rgba(255, 255, 255, 0.05) !default;
$picklistListItemActiveBorderColor:$highlightBg !default;

//schedule
$fullCalendarEventBg:$primaryDarkColor !default;
$fullCalendarEventBorderColor:$primaryDarkColor !default;
$fullCalendarEventBorder:1px solid $primaryDarkColor !default;
$fullCalendarEventTextColor:$primaryTextColor !default;

//tree
$treeContainerPadding:0.286rem !default;
$treeNodePadding:0.143rem !default;
$treeNodeContentPadding:0.429rem 0.571rem !default;
$treeNodeChildrenPadding:0 0 0 1rem !default;
$treeNodeIconColor:$shade000 !default;

//timeline
$timelineVerticalEventContentPadding:0 1rem !default;
$timelineHorizontalEventContentPadding:1rem 0 !default;
$timelineEventMarkerWidth:1rem !default;
$timelineEventMarkerHeight:1rem !default;
$timelineEventMarkerBorderRadius:50% !default;
$timelineEventMarkerBorder:2px solid $primaryColor !default;
$timelineEventMarkerBackground:$shade500 !default;
$timelineEventConnectorSize:2px !default;
$timelineEventColor:$shade500 !default;

//org chart
$organizationChartConnectorColor:$shade100 !default;

//message
$messageMargin:1rem 0 !default;
$messagePadding:1.143rem 1.357rem !default;
$messageBorderWidth:0 0 0 20px !default;
$messageIconFontSize:1.286rem !default;
$messageTextFontSize:1rem !default;
$messageTextFontWeight:400 !default;

//inline message
$inlineMessagePadding:$inputPadding !default;
$inlineMessageMargin:0 !default;
$inlineMessageIconFontSize:1.286rem  !default;
$inlineMessageTextFontSize:1rem !default;
$inlineMessageBorderWidth:0 0 0 20px !default;

//toast
$toastIconFontSize:1.286rem !default;
$toastMessageTextMargin:0 0 0 1rem !default;
$toastMargin:0 0 1rem 0 !default;
$toastPadding:1.143rem 1.357rem !default;
$toastBorderWidth:0 0 0 20px !default;
$toastShadow:none !default;
$toastOpacity:.9 !default;
$toastTitleFontWeight:400 !default;
$toastDetailMargin:$inlineSpacing 0 0 0 !default;

//severities
$infoMessageBg:$shade500 !default;
$infoMessageBorder:solid #873EFE !default;
$infoMessageTextColor:$shade000 !default;
$infoMessageIconColor:$shade000 !default;
$successMessageBg:$shade500 !default;
$successMessageBorder:solid #0BD18A !default;
$successMessageTextColor:$shade000 !default;
$successMessageIconColor:$shade000 !default;
$warningMessageBg:$shade500 !default;
$warningMessageBorder:solid #EEE500 !default;
$warningMessageTextColor:$shade000 !default;
$warningMessageIconColor:$shade000 !default;
$errorMessageBg:$shade500 !default;
$errorMessageBorder:solid #FC6161 !default;
$errorMessageTextColor:$shade000 !default;
$errorMessageIconColor:$shade000 !default;

//overlays
$overlayContentBorder:0 none !default;
$overlayContentBg:#252636 !default;
$overlayContainerShadow:0px 10px 30px rgba(0, 0, 0, 0.3) !default;

//dialog
$dialogBorderRadius:20px;
$dialogHeaderBg:#252636 !default;
$dialogHeaderBorder:0 none !default;
$dialogHeaderTextColor:$shade000 !default;
$dialogHeaderFontWeight:500 !default;
$dialogHeaderFontSize:1.143rem !default;
$dialogHeaderPadding:1.286rem 1.714rem !default;
$dialogContentPadding:0 1.714rem 1.714rem 1.714rem !default;
$dialogFooterBorder:0 none !default;
$dialogFooterPadding:0 1.714rem 1.714rem 1.714rem !default;

//confirmpopup
$confirmPopupContentPadding:$panelContentPadding !default;
$confirmPopupFooterPadding:0 1rem 1rem 1rem !default;

//tooltip
$tooltipBg:$solidSurfaceColor !default;
$tooltipTextColor:$shade000 !default;
$tooltipPadding:$inputPadding !default;

//steps
$stepsItemBg:transparent !default;
$stepsItemBorder:0 none !default;
$stepsItemTextColor:$shade200 !default;
$stepsItemNumberBg:$shade600 !default;
$stepsItemNumberWidth:1.714rem !default;
$stepsItemNumberHeight:1.714rem !default;
$stepsItemNumberFontSize:1.143rem !default;
$stepsItemNumberColor:$shade200 !default;
$stepsItemNumberBorderRadius:12px !default;
$stepsItemHoverBg:$shade800 !default;
$stepsItemHoverTextColor:$shade000 !default;
$stepsItemActiveFontWeight:400 !default;
$stepsItemActiveBg:$highlightBg !default;
$stepsItemNumberActiveTextColor:$highlightTextColor !default;
$stepsItemActiveTextColor:$shade000 !default;
$stepsItemActiveShadow:0px 0px 10px rgba($highlightBg, 0.3) !default;

//progressbar
$progressBarHeight:0.571rem !default;
$progressBarBorder:0 none !default;
$progressBarBg:$shade600 !default;
$progressBarValueBg:$primaryColor !default;
$progressBarValueTextColor:$primaryTextColor !default;

//menu (e.g. menu, menubar, tieredmenu)
$menuWidth:12.5rem !default;
$menuBg:transparent !default;
$menuBorder:1px solid $shade700 !default;
$menuTextColor:$shade100 !default;
$menuitemPadding:0.571rem 0.429rem !default;
$menuitemBorderRadius:$borderRadius !default;
$menuitemBorder:1px solid transparent !default;
$menuitemTextColor:$shade100 !default;
$menuitemIconColor:$shade100 !default;
$menuitemTextHoverColor:$shade000 !default;
$menuitemIconHoverColor:$shade000 !default;
$menuitemHoverBg:$shade500 !default;
$menuitemFocusBorderColor:$shade900 !default;
$menuitemTextActiveColor:$shade000 !default;
$menuitemIconActiveColor:$shade000 !default;
$menuitemActiveBg: $shade500 !default;
$menuitemSubmenuIconFontSize:.875rem !default;
$submenuHeaderMargin:0 !default;
$submenuHeaderPadding:0.571rem 0.429rem !default;
$submenuHeaderBg:transparent !default;
$submenuHeaderTextColor:$shade200 !default;
$submenuHeaderBorderRadius:$borderRadius !default;
$submenuHeaderFontWeight:500 !default;
$submenuHeaderFontSize:0.857rem !default;
$overlayMenuBg:$solidSurfaceColor !default;
$overlayMenuBorder:1px solid transparent !default;
$overlayMenuShadow:none !default;
$verticalMenuPadding:0.429rem !default;
$verticalMenuitemMargin:0;
$menuSeparatorMargin:.25rem 0 !default;

$panelmenuHeaderTextColor: $shade200;

$breadcrumbPadding:0.857rem !default;
$breadcrumbBg:$menuBg !default;
$breadcrumbBorder:$menuBorder !default;
$breadcrumbItemTextColor:$menuitemTextColor !default;
$breadcrumbItemIconColor:$menuitemIconColor !default;
$breadcrumbLastItemTextColor:$menuitemTextColor !default;
$breadcrumbLastItemIconColor:$menuitemIconColor !default;
$breadcrumbSeparatorColor:$menuitemTextColor !default;

$horizontalMenuPadding:0.857rem !default;
$horizontalMenuBg:$menuBg !default;
$horizontalMenuBorder:$menuBorder !default;
$horizontalMenuTextColor:$menuTextColor !default;
$horizontalMenuRootMenuitemPadding:$menuitemPadding !default;
$horizontalMenuRootMenuitemBorderRadius:$borderRadius !default;
$horizontalMenuRootMenuitemTextColor:$menuitemTextColor !default;
$horizontalMenuRootMenuitemIconColor:$menuitemIconColor !default;
$horizontalMenuRootMenuitemTextHoverColor:$menuitemTextHoverColor !default;
$horizontalMenuRootMenuitemIconHoverColor:$menuitemIconHoverColor !default;
$horizontalMenuRootMenuitemHoverBg:$menuitemHoverBg !default;
$horizontalMenuRootMenuitemTextActiveColor:$menuitemTextActiveColor !default;
$horizontalMenuRootMenuitemIconActiveColor:$menuitemIconActiveColor !default;
$horizontalMenuRootMenuitemActiveBg:$menuitemActiveBg !default;

//badge and tag
$badgeBg:$primaryColor !default;
$badgeTextColor:$primaryTextColor !default;
$badgeMinWidth:1.429rem !default;
$badgeHeight:1.429rem !default;
$badgeFontWeight:500 !default;
$badgeFontSize:1rem !default;

$tagPadding:0 0.429rem !default;

//carousel
$carouselIndicatorsPadding:1rem !default;
$carouselIndicatorBg:$shade600 !default;
$carouselIndicatorHoverBg:$shade800 !default;
$carouselIndicatorBorderRadius:3px !default;
$carouselIndicatorWidth:1.429rem !default;
$carouselIndicatorHeight:0.572rem !default;
$carouselIndicatorActiveBg: $shade100 !default;
$carouselIndicatorActiveTextColor: $shade000 !default;

//galleria
$galleriaMaskBg:rgba(0,0,0,0.9) !default;
$galleriaCloseIconMargin:.5rem !default;
$galleriaCloseIconFontSize:2rem !default;
$galleriaCloseIconBg:transparent !default;
$galleriaCloseIconColor:$shade000 !default;
$galleriaCloseIconHoverBg:rgba(255,255,255,0.1) !default;
$galleriaCloseIconHoverColor:$shade000 !default;
$galleriaCloseIconWidth:4rem !default;
$galleriaCloseIconHeight:4rem !default;
$galleriaCloseIconBorderRadius:50% !default;

$galleriaItemNavigatorBg:transparent !default;
$galleriaItemNavigatorColor:$shade000 !default;
$galleriaItemNavigatorMargin:0 .5rem !default;
$galleriaItemNavigatorFontSize:2rem !default;
$galleriaItemNavigatorHoverBg:rgba(255,255,255,0.1) !default;
$galleriaItemNavigatorHoverColor:$shade000 !default;
$galleriaItemNavigatorWidth:4rem !default;
$galleriaItemNavigatorHeight:4rem !default;
$galleriaItemNavigatorBorderRadius:$borderRadius !default;

$galleriaCaptionBg:rgba(0,0,0,.5) !default;
$galleriaCaptionTextColor:#f8f9fa !default;
$galleriaCaptionPadding:1rem !default;

$galleriaIndicatorsPadding:1rem !default;
$galleriaIndicatorBg:$shade600 !default;
$galleriaIndicatorHoverBg:$shade800  !default;
$galleriaIndicatorBorderRadius:3px !default;
$galleriaIndicatorWidth:1.429rem !default;
$galleriaIndicatorHeight:0.286rem !default;
$galleriaIndicatorsBgOnItem:rgba(0,0,0,.5) !default;
$galleriaIndicatorBgOnItem:$shade100 !default;
$galleriaIndicatorHoverBgOnItem:$shade000 !default;
$galleriaIndicatorActiveBg: $shade200 !default;
$galleriaIndicatorActiveTextColor: $shade100 !default;

$galleriaThumbnailContainerBg:$solidSurfaceColor !default;
$galleriaThumbnailContainerPadding:1rem .25rem !default;
$galleriaThumbnailNavigatorBg:transparent !default;
$galleriaThumbnailNavigatorColor:$shade000 !default;
$galleriaThumbnailNavigatorHoverBg:rgba(255,255,255,0.1) !default;
$galleriaThumbnailNavigatorHoverColor:$shade000 !default;
$galleriaThumbnailNavigatorBorderRadius:50% !default;
$galleriaThumbnailNavigatorWidth:2rem !default;
$galleriaThumbnailNavigatorHeight:2rem !default;

//divider
$dividerHorizontalMargin:1rem 0;
$dividerHorizontalPadding:0 1rem;
$dividerVerticalMargin:0 1rem;
$dividerVerticalPadding:1rem 0;
$dividerSize:1px;
$dividerColor:$shade700;

//avatar
$avatarBg:$shade500;
$avatarTextColor:$textColor;

//chip
$chipBg:$shade500;
$chipTextColor:$textColor;
$chipBorderRadius: 16px;

//scrollTop
$scrollTopBg:$highlightBg;
$scrollTopHoverBg:scale-color($highlightBg, $alpha: 24%);
$scrollTopWidth:3rem;
$scrollTopHeight:3rem;
$scrollTopBorderRadius:50%;
$scrollTopFontSize:1.5rem;
$scrollTopTextColor:$highlightTextColor;

//skeleton
$skeletonBg:rgba(255,255,255,.06);
$skeletonAnimationBg:rgba(255,255,255,.04);

//splitter
$splitterGutterBg:$shade700;
$splitterGutterHandleBg:$shade700;

//speeddial
$speedDialButtonWidth: 4rem !default;
$speedDialButtonHeight: 4rem !default;
$speedDialButtonIconFontSize: 1.3rem !default;
$speedDialActionWidth: 3rem !default;
$speedDialActionHeight: 3rem !default;
$speedDialActionBg: $shade000 !default;
$speedDialActionHoverBg: $shade100 !default;
$speedDialActionTextColor: $shade900 !default;
$speedDialActionTextHoverColor: $shade900 !default;

//dock
$dockActionWidth: 4rem !default;
$dockActionHeight: 4rem !default;
$dockItemPadding: .5rem !default;
$dockCurrentItemMargin: 1.5rem !default;
$dockFirstItemsMargin: 1.3rem !default;
$dockSecondItemsMargin: 0.9rem !default;
$dockBg: rgba(255,255,255,.1) !default;
$dockBorder: 1px solid rgba(255,255,255,0.2) !default;
$dockPadding: .5rem .5rem !default;
$dockBorderRadius: .5rem !default;

//image
$imageMaskBg:rgba(0,0,0,0.9) !default;
$imagePreviewToolbarPadding:1rem !default;
$imagePreviewIndicatorColor:#f8f9fa !default;
$imagePreviewIndicatorBg:rgba(0,0,0,0.5) !default;
$imagePreviewActionIconBg:transparent !default;
$imagePreviewActionIconColor:#f8f9fa !default;
$imagePreviewActionIconHoverBg:rgba(255,255,255,0.1) !default;
$imagePreviewActionIconHoverColor:#f8f9fa !default;
$imagePreviewActionIconWidth:3rem !default;
$imagePreviewActionIconHeight:3rem !default;
$imagePreviewActionIconFontSize:1.5rem !default;
$imagePreviewActionIconBorderRadius:50% !default;

:root {
    --surface-a:#{$shade200};
    --surface-b:#{$shade500};
    --surface-c:#{$shade600};
    --surface-d:#{$shade700};
    --surface-e:#{$shade800};
    --surface-f:#{$shade900};
    --text-color:#{$shade000};
    --text-color-secondary:#{$shade100};
    --primary-color:#{$primaryColor};
    --primary-color-text:#{$primaryTextColor};
    --font-family:#{$fontFamily};
    --surface-0: #0a061a;
    --surface-50: #231f31;
    --surface-100: #3b3848;
    --surface-200: #54515f;
    --surface-300: #6c6a76;
    --surface-400: #85838d;
    --surface-500: #9d9ba3;
    --surface-600: #b6b4ba;
    --surface-700: #cecdd1;
    --surface-800: #e7e6e8;
    --surface-900: #ffffff;
    --gray-50: #e7e6e8;
    --gray-100: #cecdd1;
    --gray-200: #b6b4ba;
    --gray-300: #9d9ba3;
    --gray-400: #85838d;
    --gray-500: #6c6a76;
    --gray-600: #54515f;
    --gray-700: #3b3848;
    --gray-800: #231f31;
    --gray-900: #0a061a;
    --content-padding:#{$panelContentPadding};
    --inline-spacing:#{$inlineSpacing};
    --border-radius:#{$borderRadius};
    --surface-ground:linear-gradient(180deg, #2E323F 0%, #0A061A 100%);
    --surface-section:linear-gradient(180deg, #2E323F 0%, #0A061A 100%);
    --surface-card:rgba(255, 255, 255, 0.05);
    --surface-overlay:linear-gradient(180deg, #2E323F 0%, #0A061A 100%);
    --surface-border:rgba(255, 255, 255, 0.15);
    --surface-hover:rgba(255, 255, 255, 0.05);
    --focus-ring: #{$focusShadow};
    --maskbg: #{$maskBg};
}    
</code></pre>
</div>

                <h4>Menu Modes</h4>
                <p>Menu has 5 modes; static, overlay, slim, horizontal and sidebar. Layout wrapper element in App.vue is 
                    used to define which mode to use by adding specific classes. List below indicates the style classes for each mode.</p>

                <ul>
                    <li>Static: "layout-wrapper layout-menu-static"</li>
                    <li>Overlay: "layout-wrapper layout-menu-overlay"</li>
                    <li>Slim: "layout-wrapper layout-menu-slim"</li>
                    <li>Horizontal: "layout-wrapper layout-menu-horizontal"</li>
                    <li>Sidebar: "layout-wrapper layout-sidebar"</li>
                </ul>

                <p>It is also possible to leave the choice to the user by keeping the preference at a component and using an expression to bind it so that user can switch between modes. Sample
                    application has an example implementation of such use case. Refer to App.vue for an example.</p>

<pre v-code><code><template>
&lt;div class="layout-wrapper" :class="{'layout-overlay':menuMode === 'overlay',
                                        'layout-overlay-active':overlayMenuActive}"&gt;&lt;/div&gt;
</template>
</code></pre>

                <h4>Grid CSS</h4>
                <p>Atlantis uses PrimeVue Flex Grid CSS throughout the demos such as Dashboard, however any Grid library can be used with it since Atlantis Layout itself does not depend on PrimeFlex CSS.</p>

                <h4>Customizing Styles</h4>
                <p>It is suggested to add your customizations in the following sass files under the override folder instead of adding them to the
                    scss files under sass folder to avoid maintenance issues after an update.</p>

                <ul>
                    <li><b>_layout_variables</b>: Variables of the layout.</li>
                    <li><b>_layout_styles</b>: Styles for the layout.</li>
                    <li><b>_theme_variables</b>: Variables of the theme.</li>
                    <li><b>_theme_styles</b>: Styles for the theme.</li>
                </ul>

                <h4>Migration Guide</h4>
                <p>Every change is included in <b>CHANGELOG.md</b> file at the root folder of the distribution along with the instructions to update.</p>
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style scoped lang="scss">
@import '../assets/demo/styles/documentation.scss';

.docs li {
    line-height: 1.5;
}
</style>
