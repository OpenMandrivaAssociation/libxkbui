%define name	libxkbui
%define version	1.0.2
%define release	%mkrel 11

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
Patch0:		libxkbui-1.0.2-drop-xt.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1

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

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libxkbui.so
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
%{_libdir}/libxkbui.*a

#-----------------------------------------------------------

%prep
%setup -q -n libxkbui-%{version}
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxkbui.so.1
%{_libdir}/libxkbui.so.1.0.0



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-10mdv2011.0
+ Revision: 662424
- mass rebuild

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 1.0.2-9
+ Revision: 636542
- it has nothing to do with xt

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2011.0
+ Revision: 602620
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2010.1
+ Revision: 520966
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425929
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 223078
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2008.1
+ Revision: 150861
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 04 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-3mdv2008.0
+ Revision: 58828
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

