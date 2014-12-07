%define major	1
%define libname	%mklibname xkbui %{major}
%define devname	%mklibname xkbui -d

Summary:	The xkbui Library
Name:		libxkbui
Version:	1.0.2
Release:	20
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Patch0:		libxkbui-1.0.2-drop-xt.patch
Patch1:		libxkbui-automake-1.13.patch
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1

%track
prog %{name} = {
	url = http://xorg.freedesktop.org/releases/individual/lib/
	regex = %{name}-(__VER__)\.tar\.bz2
	version = %{version}
}

%description
The xkbui Library

%package -n %{libname}
Summary:	The xkbui Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The xkbui Library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libxkbui-%{version}
%patch0 -p0
%patch1 -p1 -b .am113~
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxkbui.so.%{major}*

%files -n %{devname}
%{_libdir}/libxkbui.so
%{_libdir}/pkgconfig/xkbui.pc
%{_includedir}/X11/extensions/XKBui.h

