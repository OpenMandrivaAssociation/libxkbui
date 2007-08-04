%define name	libxkbui
%define version	1.0.2
%define release	%mkrel 3

%define libname		%mklibname xkbui 1
%define develname	%mklibname xkbui -d
%define staticname	%mklibname xkbui -d -s

Name:		%{name}
Summary:	The xkbui Library
Version:	%{version}
Release:	%{release}
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbui Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The xkbui Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The xkbui Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}
Requires: libx11-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname xkbui 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libxkbui.so
%{_libdir}/libxkbui.la
%{_libdir}/pkgconfig/xkbui.pc
%{_includedir}/X11/extensions/XKBui.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname xkbui 1 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libxkbui.a

#-----------------------------------------------------------

%prep
%setup -q -n libxkbui-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxkbui.so.1
%{_libdir}/libxkbui.so.1.0.0

