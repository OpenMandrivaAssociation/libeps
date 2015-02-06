%define	rname eps

%define	major 0
%define libname %mklibname %{rname} %{major}
%define develname %mklibname %{rname} -d

Summary:	EPS (Email Parsing System) library
Name:		libeps
Version:	1.5
Release:	7
Group:		System/Libraries
License:	GPL
URL:		http://www.inter7.com/
Source0:	http://www.inter7.com/eps/%{rname}-%{version}.tar.bz2
Patch0:		eps-1.5-shared.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
EPS (Email Parsing System) is intended to give people the ability
to write their own email processing tools. Whether you want to
process incoming and outgoing emails, or just analyze a message,
this package is intended to aid in that endeavor. 

%package -n	%{libname}
Summary:	Shared EPS (Email Parsing System) library
Group:          System/Libraries

%description -n	%{libname}
EPS (Email Parsing System) is intended to give people the ability
to write their own email processing tools. Whether you want to
process incoming and outgoing emails, or just analyze a message,
this package is intended to aid in that endeavor. 

%package -n	%{develname}
Summary:	Static library and header files for the libeps library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{rname}-devel = %{version}-%{release}
Provides:	lib%{rname}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{rname} 0 -d}

%description -n	%{develname}
EPS (Email Parsing System) is intended to give people the ability
to write their own email processing tools. Whether you want to
process incoming and outgoing emails, or just analyze a message,
this package is intended to aid in that endeavor. 

This package contains the static libeps library and its header files
needed to compile applications such as stegdetect, etc.

%prep

%setup -q -n %{rname}-%{version}
%patch0 -p0

%build

make CFLAGS="%{optflags} -fPIC -DPIC"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/eps

install -m0644 libeps.a %{buildroot}%{_libdir}/
install -m0755 libeps.so.%{major} %{buildroot}%{_libdir}/
ln -snf libeps.so.%{major} %{buildroot}%{_libdir}/libeps.so
install -m0644 *.h %{buildroot}%{_includedir}/eps/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc doc/* mess ChangeLog TODO
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/eps
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-6mdv2011.0
+ Revision: 620120
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2010.0
+ Revision: 429727
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-4mdv2009.0
+ Revision: 239060
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5-3mdv2008.0
+ Revision: 83753
- new devel naming


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdv2007.0
+ Revision: 93751
- Import libeps

* Sat Apr 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdk
- rebuild

* Wed Feb 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.5-1mdk
- initial Mandrakelinux package

