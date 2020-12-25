%define Werror_cflags %nil
%define _disable_rebuild_configure 1

Summary:	VICE, the Versatile Commodore Emulator
Name:		vice
Version:	3.5
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://vice-emu.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/vice-emu/releases/vice-%{version}.tar.gz
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
BuildRequires:	bdftopcf
BuildRequires:	flex
BuildRequires:	mkfontdir
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	readline-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	xa
BuildRequires:	byacc
Requires:	vice-binaries = %{EVRD}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%files
%doc README
%doc %{_docdir}/vice
%{_datadir}/vice
%{_iconsdir}/hicolor/*/apps/*.png

#----------------------------------------------------------------------------

%package sdl
Summary:	SDL set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{EVRD}
Provides:	vice-binaries = %{EVRD}

%description sdl
SDL set of vice emulators binaries.

%files sdl
%{_bindir}/*-sdl
%{_datadir}/applications/*-sdl.desktop

#----------------------------------------------------------------------------

%package gtk
Summary:	GTK set of vice emulators binaries
Group:		Emulators
Requires:	%{name} = %{EVRD}
Provides:	vice-binaries = %{EVRD}

%description gtk
GTK set of vice emulators binaries.

%files gtk
%{_bindir}/*
%exclude %{_bindir}/*-sdl
%{_datadir}/applications/vice-org-*.desktop

#----------------------------------------------------------------------------

%prep
%autosetup -p1
# --disable-option-checking is needed because the configure
# macro adds --disable-static, --disable-rpath and a few other
# generic autoconf-isms
%define common_args \\\
	--enable-fullscreen \\\
	--enable-external-ffmpeg \\\
	--enable-ethernet \\\
	--with-ui-threads \\\
	--with-sdlsound \\\
	--disable-pdf-docs \\\
	--enable-lame \\\
	--enable-midi \\\
	--enable-cpuhistory \\\
	--enable-x64 \\\
	--enable-x64-image \\\
	--with-flac \\\
	--with-mpg123 \\\
	--with-vorbis

#	--disable-option-checking \\\

export CONFIGURE_TOP=`pwd`

mkdir sdl
cd sdl
%configure \
	%{common_args} \
	--enable-sdlui2
cd ..

mkdir gtk
cd gtk
%configure \
	%{common_args} \
	--enable-native-gtk3ui \
	--enable-desktop-files
cd ..

%build
%make_build -C sdl
%make_build -C gtk

%install
%make_install -C sdl
for i in %{buildroot}%{_bindir}/*; do
	mv $i ${i}-sdl
done
%make_install -C gtk
mkdir -p %{buildroot}%{_datadir}/applications
cp -a gtk/src/arch/gtk3/data/unix/*.desktop %{buildroot}%{_datadir}/applications/

#xdg menus
#============SDL============
cat > %{buildroot}%{_datadir}/applications/mandriva-x64-sdl.desktop << EOF
[Desktop Entry]
Name=C64 Emulator (SDL)
Comment=Commodore 64 Emulator
Exec=%{_bindir}/x64-sdl %U
Icon=c64icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Game;Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-x128-sdl.desktop << EOF
[Desktop Entry]
Name=C128 Emulator (SDL)
Comment=Commodore 128 Emulator
Exec=%{_bindir}/x128-sdl %U
Icon=c128icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-xpet-sdl.desktop << EOF
[Desktop Entry]
Name=PET Emulator (SDL)
Comment=Commodore PET Emulator
Exec=%{_bindir}/xpet-sdl %U
Icon=peticon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-xvic-sdl.desktop << EOF
[Desktop Entry]
Name=VIC 20 Emulator (SDL)
Comment=Commodore VIC 20 Emulator
Exec=%{_bindir}/xvic-sdl %U
Icon=vic20icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2-sdl.desktop << EOF
[Desktop Entry]
Name=CBM2 Emulator (SDL)
Comment=Commodore BM 2 Emulator
Exec=%{_bindir}/xcbm2-sdl %U
Icon=c610icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4-sdl.desktop << EOF
[Desktop Entry]
Name=CPLUS4 Emulator (SDL)
Comment=Commodore PLUS4 Emulator
Exec=%{_bindir}/xplus4-sdl %U
Icon=plus4icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-c1541-sdl.desktop << EOF
[Desktop Entry]
Name=VICE disk image tool (SDL)
Comment=C1541 stand alone disk image maintenance program
Exec=%{_bindir}/c1541-sdl %U
Icon=commodore
Terminal=true
Type=Application
StartupNotify=true
Categories=Emulator;
EOF

cat > %{buildroot}%{_datadir}/applications/mandriva-vsid-sdl.desktop << EOF
[Desktop Entry]
Name=VSID music player (SDL)
Comment=VICE SID music player for Commodore tunes
Exec=%{_bindir}/vsid-sdl %U
Icon=commodore
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;Player;
EOF
#============SDL============

#install icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}/hicolor/32x32/apps
tar xjf %{SOURCE2} -C %{buildroot}%{_iconsdir}/hicolor/48x48/apps
tar xjf %{SOURCE3} -C %{buildroot}%{_iconsdir}/hicolor/16x16/apps
