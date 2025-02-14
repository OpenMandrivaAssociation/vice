%define Werror_cflags %nil
%define _disable_rebuild_configure 1
%define debug_package %{nil}

Summary:	VICE, the Versatile Commodore Emulator
Name:		vice
Version:	3.9
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		https://vice-emu.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/vice-emu/releases/vice-%{version}.tar.gz
Patch0:		vice-build-flags.patch
BuildRequires:	bdftopcf
BuildRequires:	flex
BuildRequires:	mkfontdir
BuildRequires:	dos2unix
BuildRequires:	gettext-devel
BuildRequires:	lame-devel
BuildRequires:	giflib-devel
BuildRequires:	readline-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	xdg-utils
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	xa
BuildRequires:	byacc
BuildRequires:	locales-extra-charsets
Requires:	vice-binaries = %{EVRD}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%files
%doc %{_docdir}/vice
%{_datadir}/vice
%{_datadir}/icons/hicolor/*/apps/*

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
%autosetup -p1 -n %{name}-%{version}
# --disable-option-checking is needed because the configure
# macro adds --disable-static, --disable-rpath and a few other
# generic autoconf-isms
%define common_args \\\
	--enable-fullscreen \\\
	--disable-ffmpeg \\\
	--enable-ethernet \\\
	--with-ui-threads \\\
	--with-sdlsound \\\
	--disable-pdf-docs \\\
	--disable-sdl1ui \\\
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
	--enable-sdl2ui
cd ..

mkdir gtk
cd gtk
%configure \
	%{common_args} \
	--enable-gtk3ui \
	--enable-desktop-files
find . -name Makefile |xargs sed -i -e 's,-lOpenGL,-lOpenGL -lGLX,'
cd ..


%build
export CC=gcc
export CXX=g++
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
Icon=C64_1024
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
Icon=C128_1024
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
Icon=PET_256
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
Icon=VIC20_1024
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
Icon=CBM2_1024
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
Icon=Plus4_1024
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
Icon=CBM_Logo
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
Icon=SID_1024
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;Player;
EOF
#============SDL============

# Install icons for the desktop files
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp data/common/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
