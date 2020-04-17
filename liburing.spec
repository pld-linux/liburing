Summary:	Linux-native io_uring I/O access library
Summary(pl.UTF-8):	Biblioteka natywnego dla Linuksa dostępu we/wy io_uring
Name:		liburing
Version:	0.5
Release:	1
License:	LGPL v2+ or MIT
Group:		Libraries
Source0:	https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
# Source0-md5:	98d9ed88aa260cc0515410f344d57319
URL:		https://git.kernel.dk/cgit/liburing/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%description -l pl.UTF-8
Biblioteka udostępnia w sposób szybki i wydajny natywne,
asynchroniczne operacje we/wy dla jądra Linuksa, zarówno buforowane,
jak i O_DIRECT.

%package devel
Summary:	Header files and development documentation for liburing
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programistyczna do biblioteki liburing
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for Linux-native io_uring I/O access library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki dostępu do natywnego dla Linuksa we/wy
io_uring.

%package static
Summary:	Static liburing library
Summary(pl.UTF-8):	Statyczna biblioteka liburing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liburing library.

%description static -l pl.UTF-8
Statyczna biblioteka liburing.

%prep
%setup -q

%build
# not autoconf configure
./configure \
	--cc="%{__cc}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libdevdir=%{_libdir} \
	--mandir=%{_mandir} \
	--includedir=%{_includedir}
 
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/liburing.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liburing.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liburing.so
%{_includedir}/liburing
%{_includedir}/liburing.h
%{_pkgconfigdir}/liburing.pc
%{_mandir}/man2/io_uring_*.2*

%files static
%defattr(644,root,root,755)
%{_libdir}/liburing.a
