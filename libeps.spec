%define	rname eps

%define	major 0
%define libname %mklibname %{rname} %{major}
%define develname %mklibname %{rname} -d

Summary:	EPS (Email Parsing System) library
Name:		libeps
Version:	1.5
Release:	%mkrel 3
Group:		System/Libraries
License:	GPL
URL:		http://www.inter7.com/
Source0:	http://www.inter7.com/eps/%{rname}-%{version}.tar.bz2
Patch0:		eps-1.5-shared.diff

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/eps

install -m0644 libeps.a %{buildroot}%{_libdir}/
install -m0755 libeps.so.%{major} %{buildroot}%{_libdir}/
ln -snf libeps.so.%{major} %{buildroot}%{_libdir}/libeps.so
install -m0644 *.h %{buildroot}%{_includedir}/eps/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc doc/* mess ChangeLog TODO
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/eps
%{_libdir}/*.so
%{_libdir}/*.a
